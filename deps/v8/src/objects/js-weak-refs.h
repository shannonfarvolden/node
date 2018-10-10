// Copyright 2018 the V8 project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef V8_OBJECTS_JS_WEAK_REFS_H_
#define V8_OBJECTS_JS_WEAK_REFS_H_

#include "src/objects/js-objects.h"

// Has to be the last include (doesn't have include guards):
#include "src/objects/object-macros.h"

namespace v8 {
namespace internal {

class JSWeakCell;

// WeakFactory object from the JS Weak Refs spec proposal:
// https://github.com/tc39/proposal-weakrefs
class JSWeakFactory : public JSObject {
 public:
  DECL_PRINTER(JSWeakFactory)
  DECL_VERIFIER(JSWeakFactory)
  DECL_CAST(JSWeakFactory)

  DECL_ACCESSORS(cleanup, Object)
  DECL_ACCESSORS(active_cells, Object)
  DECL_ACCESSORS(cleared_cells, Object)

  // For storing a list of JSWeakFactory objects in NativeContext.
  DECL_ACCESSORS(next, Object)

  // Returns true if the cleared_cells list is non-empty.
  inline bool NeedsCleanup() const;

  // Get and remove the first cleared JSWeakCell from the cleared_cells
  // list. (Assumes there is one.)
  inline JSWeakCell* PopClearedCell(Isolate* isolate);

  static const int kCleanupOffset = JSObject::kHeaderSize;
  static const int kActiveCellsOffset = kCleanupOffset + kPointerSize;
  static const int kClearedCellsOffset = kActiveCellsOffset + kPointerSize;
  static const int kNextOffset = kClearedCellsOffset + kPointerSize;
  static const int kSize = kNextOffset + kPointerSize;

 private:
  DISALLOW_IMPLICIT_CONSTRUCTORS(JSWeakFactory);
};

// WeakCell object from the JS Weak Refs spec proposal.
class JSWeakCell : public JSObject {
 public:
  DECL_PRINTER(JSWeakCell)
  DECL_VERIFIER(JSWeakCell)
  DECL_CAST(JSWeakCell)

  DECL_ACCESSORS(factory, JSWeakFactory)
  DECL_ACCESSORS(target, Object)

  // For storing doubly linked lists of JSWeakCells in JSWeakFactory.
  DECL_ACCESSORS(prev, Object)
  DECL_ACCESSORS(next, Object)

  static const int kFactoryOffset = JSObject::kHeaderSize;
  static const int kTargetOffset = kFactoryOffset + kPointerSize;
  static const int kPrevOffset = kTargetOffset + kPointerSize;
  static const int kNextOffset = kPrevOffset + kPointerSize;
  static const int kSize = kNextOffset + kPointerSize;

  class BodyDescriptor;

  // Nullify is called during GC and it modifies the pointers in JSWeakCell and
  // JSWeakFactory. Thus we need to tell the GC about the modified slots via the
  // gc_notify_updated_slot function. The normal write barrier is not enough,
  // since it's disabled before GC.
  inline void Nullify(
      Isolate* isolate,
      std::function<void(HeapObject* object, Object** slot, Object* target)>
          gc_notify_updated_slot);

 private:
  DISALLOW_IMPLICIT_CONSTRUCTORS(JSWeakCell);
};

class JSWeakFactoryCleanupIterator : public JSObject {
 public:
  DECL_PRINTER(JSWeakFactoryCleanupIterator)
  DECL_VERIFIER(JSWeakFactoryCleanupIterator)
  DECL_CAST(JSWeakFactoryCleanupIterator)

  DECL_ACCESSORS(factory, JSWeakFactory)

  static const int kFactoryOffset = JSObject::kHeaderSize;
  static const int kSize = kFactoryOffset + kPointerSize;

 private:
  DISALLOW_IMPLICIT_CONSTRUCTORS(JSWeakFactoryCleanupIterator);
};

class JSWeakFactoryCleanupTask : public v8::Task {
 public:
  inline explicit JSWeakFactoryCleanupTask(Isolate* isolate);
  void Run() override;

 private:
  v8::Persistent<v8::Context> native_context_;
  Isolate* isolate_;

  DISALLOW_IMPLICIT_CONSTRUCTORS(JSWeakFactoryCleanupTask);
};

}  // namespace internal
}  // namespace v8

#include "src/objects/object-macros-undef.h"

#endif  // V8_OBJECTS_JS_WEAK_REFS_H_
