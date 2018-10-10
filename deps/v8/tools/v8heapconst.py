# Copyright 2018 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  34: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  42: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  64: "STRING_TYPE",
  65: "CONS_STRING_TYPE",
  66: "EXTERNAL_STRING_TYPE",
  67: "SLICED_STRING_TYPE",
  69: "THIN_STRING_TYPE",
  72: "ONE_BYTE_STRING_TYPE",
  73: "CONS_ONE_BYTE_STRING_TYPE",
  74: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  75: "SLICED_ONE_BYTE_STRING_TYPE",
  77: "THIN_ONE_BYTE_STRING_TYPE",
  82: "EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  98: "UNCACHED_EXTERNAL_STRING_TYPE",
  106: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  114: "UNCACHED_EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  128: "SYMBOL_TYPE",
  129: "HEAP_NUMBER_TYPE",
  130: "BIGINT_TYPE",
  131: "ODDBALL_TYPE",
  132: "MAP_TYPE",
  133: "CODE_TYPE",
  134: "MUTABLE_HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "BYTECODE_ARRAY_TYPE",
  138: "FREE_SPACE_TYPE",
  139: "FIXED_INT8_ARRAY_TYPE",
  140: "FIXED_UINT8_ARRAY_TYPE",
  141: "FIXED_INT16_ARRAY_TYPE",
  142: "FIXED_UINT16_ARRAY_TYPE",
  143: "FIXED_INT32_ARRAY_TYPE",
  144: "FIXED_UINT32_ARRAY_TYPE",
  145: "FIXED_FLOAT32_ARRAY_TYPE",
  146: "FIXED_FLOAT64_ARRAY_TYPE",
  147: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  148: "FIXED_BIGINT64_ARRAY_TYPE",
  149: "FIXED_BIGUINT64_ARRAY_TYPE",
  150: "FIXED_DOUBLE_ARRAY_TYPE",
  151: "FEEDBACK_METADATA_TYPE",
  152: "FILLER_TYPE",
  153: "ACCESS_CHECK_INFO_TYPE",
  154: "ACCESSOR_INFO_TYPE",
  155: "ACCESSOR_PAIR_TYPE",
  156: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  157: "ALLOCATION_MEMENTO_TYPE",
  158: "ASYNC_GENERATOR_REQUEST_TYPE",
  159: "DEBUG_INFO_TYPE",
  160: "FUNCTION_TEMPLATE_INFO_TYPE",
  161: "INTERCEPTOR_INFO_TYPE",
  162: "INTERPRETER_DATA_TYPE",
  163: "MODULE_INFO_ENTRY_TYPE",
  164: "MODULE_TYPE",
  165: "OBJECT_TEMPLATE_INFO_TYPE",
  166: "PROMISE_CAPABILITY_TYPE",
  167: "PROMISE_REACTION_TYPE",
  168: "PROTOTYPE_INFO_TYPE",
  169: "SCRIPT_TYPE",
  170: "STACK_FRAME_INFO_TYPE",
  171: "TUPLE2_TYPE",
  172: "TUPLE3_TYPE",
  173: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  174: "WASM_DEBUG_INFO_TYPE",
  175: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  176: "CALLABLE_TASK_TYPE",
  177: "CALLBACK_TASK_TYPE",
  178: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  179: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  180: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  181: "MICROTASK_QUEUE_TYPE",
  182: "ALLOCATION_SITE_TYPE",
  183: "FIXED_ARRAY_TYPE",
  184: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  185: "HASH_TABLE_TYPE",
  186: "ORDERED_HASH_MAP_TYPE",
  187: "ORDERED_HASH_SET_TYPE",
  188: "NAME_DICTIONARY_TYPE",
  189: "GLOBAL_DICTIONARY_TYPE",
  190: "NUMBER_DICTIONARY_TYPE",
  191: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  192: "STRING_TABLE_TYPE",
  193: "EPHEMERON_HASH_TABLE_TYPE",
  194: "SCOPE_INFO_TYPE",
  195: "SCRIPT_CONTEXT_TABLE_TYPE",
  196: "AWAIT_CONTEXT_TYPE",
  197: "BLOCK_CONTEXT_TYPE",
  198: "CATCH_CONTEXT_TYPE",
  199: "DEBUG_EVALUATE_CONTEXT_TYPE",
  200: "EVAL_CONTEXT_TYPE",
  201: "FUNCTION_CONTEXT_TYPE",
  202: "MODULE_CONTEXT_TYPE",
  203: "NATIVE_CONTEXT_TYPE",
  204: "SCRIPT_CONTEXT_TYPE",
  205: "WITH_CONTEXT_TYPE",
  206: "WEAK_FIXED_ARRAY_TYPE",
  207: "DESCRIPTOR_ARRAY_TYPE",
  208: "TRANSITION_ARRAY_TYPE",
  209: "CALL_HANDLER_INFO_TYPE",
  210: "CELL_TYPE",
  211: "CODE_DATA_CONTAINER_TYPE",
  212: "FEEDBACK_CELL_TYPE",
  213: "FEEDBACK_VECTOR_TYPE",
  214: "LOAD_HANDLER_TYPE",
  215: "PRE_PARSED_SCOPE_DATA_TYPE",
  216: "PROPERTY_ARRAY_TYPE",
  217: "PROPERTY_CELL_TYPE",
  218: "SHARED_FUNCTION_INFO_TYPE",
  219: "SMALL_ORDERED_HASH_MAP_TYPE",
  220: "SMALL_ORDERED_HASH_SET_TYPE",
  221: "STORE_HANDLER_TYPE",
  222: "UNCOMPILED_DATA_WITHOUT_PRE_PARSED_SCOPE_TYPE",
  223: "UNCOMPILED_DATA_WITH_PRE_PARSED_SCOPE_TYPE",
  224: "WEAK_ARRAY_LIST_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_VALUE_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1064: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1065: "JS_DATE_TYPE",
  1066: "JS_ERROR_TYPE",
  1067: "JS_GENERATOR_OBJECT_TYPE",
  1068: "JS_MAP_TYPE",
  1069: "JS_MAP_KEY_ITERATOR_TYPE",
  1070: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1071: "JS_MAP_VALUE_ITERATOR_TYPE",
  1072: "JS_MESSAGE_OBJECT_TYPE",
  1073: "JS_PROMISE_TYPE",
  1074: "JS_REGEXP_TYPE",
  1075: "JS_REGEXP_STRING_ITERATOR_TYPE",
  1076: "JS_SET_TYPE",
  1077: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1078: "JS_SET_VALUE_ITERATOR_TYPE",
  1079: "JS_STRING_ITERATOR_TYPE",
  1080: "JS_WEAK_CELL_TYPE",
  1081: "JS_WEAK_FACTORY_CLEANUP_ITERATOR_TYPE",
  1082: "JS_WEAK_FACTORY_TYPE",
  1083: "JS_WEAK_MAP_TYPE",
  1084: "JS_WEAK_SET_TYPE",
  1085: "JS_TYPED_ARRAY_TYPE",
  1086: "JS_DATA_VIEW_TYPE",
  1087: "JS_INTL_V8_BREAK_ITERATOR_TYPE",
  1088: "JS_INTL_COLLATOR_TYPE",
  1089: "JS_INTL_DATE_TIME_FORMAT_TYPE",
  1090: "JS_INTL_LIST_FORMAT_TYPE",
  1091: "JS_INTL_LOCALE_TYPE",
  1092: "JS_INTL_NUMBER_FORMAT_TYPE",
  1093: "JS_INTL_PLURAL_RULES_TYPE",
  1094: "JS_INTL_RELATIVE_TIME_FORMAT_TYPE",
  1095: "JS_INTL_SEGMENTER_TYPE",
  1096: "WASM_EXCEPTION_TYPE",
  1097: "WASM_GLOBAL_TYPE",
  1098: "WASM_INSTANCE_TYPE",
  1099: "WASM_MEMORY_TYPE",
  1100: "WASM_MODULE_TYPE",
  1101: "WASM_TABLE_TYPE",
  1102: "JS_BOUND_FUNCTION_TYPE",
  1103: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("RO_SPACE", 0x02201): (138, "FreeSpaceMap"),
  ("RO_SPACE", 0x02251): (132, "MetaMap"),
  ("RO_SPACE", 0x022d1): (131, "NullMap"),
  ("RO_SPACE", 0x02341): (207, "DescriptorArrayMap"),
  ("RO_SPACE", 0x023a1): (206, "WeakFixedArrayMap"),
  ("RO_SPACE", 0x023f1): (152, "OnePointerFillerMap"),
  ("RO_SPACE", 0x02441): (152, "TwoPointerFillerMap"),
  ("RO_SPACE", 0x024c1): (131, "UninitializedMap"),
  ("RO_SPACE", 0x02531): (8, "OneByteInternalizedStringMap"),
  ("RO_SPACE", 0x025d1): (131, "UndefinedMap"),
  ("RO_SPACE", 0x02631): (129, "HeapNumberMap"),
  ("RO_SPACE", 0x026b1): (131, "TheHoleMap"),
  ("RO_SPACE", 0x02759): (131, "BooleanMap"),
  ("RO_SPACE", 0x02831): (136, "ByteArrayMap"),
  ("RO_SPACE", 0x02881): (183, "FixedArrayMap"),
  ("RO_SPACE", 0x028d1): (183, "FixedCOWArrayMap"),
  ("RO_SPACE", 0x02921): (185, "HashTableMap"),
  ("RO_SPACE", 0x02971): (128, "SymbolMap"),
  ("RO_SPACE", 0x029c1): (72, "OneByteStringMap"),
  ("RO_SPACE", 0x02a11): (194, "ScopeInfoMap"),
  ("RO_SPACE", 0x02a61): (218, "SharedFunctionInfoMap"),
  ("RO_SPACE", 0x02ab1): (133, "CodeMap"),
  ("RO_SPACE", 0x02b01): (201, "FunctionContextMap"),
  ("RO_SPACE", 0x02b51): (210, "CellMap"),
  ("RO_SPACE", 0x02ba1): (217, "GlobalPropertyCellMap"),
  ("RO_SPACE", 0x02bf1): (135, "ForeignMap"),
  ("RO_SPACE", 0x02c41): (208, "TransitionArrayMap"),
  ("RO_SPACE", 0x02c91): (213, "FeedbackVectorMap"),
  ("RO_SPACE", 0x02d31): (131, "ArgumentsMarkerMap"),
  ("RO_SPACE", 0x02dd1): (131, "ExceptionMap"),
  ("RO_SPACE", 0x02e71): (131, "TerminationExceptionMap"),
  ("RO_SPACE", 0x02f19): (131, "OptimizedOutMap"),
  ("RO_SPACE", 0x02fb9): (131, "StaleRegisterMap"),
  ("RO_SPACE", 0x03029): (203, "NativeContextMap"),
  ("RO_SPACE", 0x03079): (202, "ModuleContextMap"),
  ("RO_SPACE", 0x030c9): (200, "EvalContextMap"),
  ("RO_SPACE", 0x03119): (204, "ScriptContextMap"),
  ("RO_SPACE", 0x03169): (196, "AwaitContextMap"),
  ("RO_SPACE", 0x031b9): (197, "BlockContextMap"),
  ("RO_SPACE", 0x03209): (198, "CatchContextMap"),
  ("RO_SPACE", 0x03259): (205, "WithContextMap"),
  ("RO_SPACE", 0x032a9): (199, "DebugEvaluateContextMap"),
  ("RO_SPACE", 0x032f9): (195, "ScriptContextTableMap"),
  ("RO_SPACE", 0x03349): (151, "FeedbackMetadataArrayMap"),
  ("RO_SPACE", 0x03399): (183, "ArrayListMap"),
  ("RO_SPACE", 0x033e9): (130, "BigIntMap"),
  ("RO_SPACE", 0x03439): (184, "ObjectBoilerplateDescriptionMap"),
  ("RO_SPACE", 0x03489): (137, "BytecodeArrayMap"),
  ("RO_SPACE", 0x034d9): (211, "CodeDataContainerMap"),
  ("RO_SPACE", 0x03529): (150, "FixedDoubleArrayMap"),
  ("RO_SPACE", 0x03579): (189, "GlobalDictionaryMap"),
  ("RO_SPACE", 0x035c9): (212, "ManyClosuresCellMap"),
  ("RO_SPACE", 0x03619): (183, "ModuleInfoMap"),
  ("RO_SPACE", 0x03669): (134, "MutableHeapNumberMap"),
  ("RO_SPACE", 0x036b9): (188, "NameDictionaryMap"),
  ("RO_SPACE", 0x03709): (212, "NoClosuresCellMap"),
  ("RO_SPACE", 0x03759): (190, "NumberDictionaryMap"),
  ("RO_SPACE", 0x037a9): (212, "OneClosureCellMap"),
  ("RO_SPACE", 0x037f9): (186, "OrderedHashMapMap"),
  ("RO_SPACE", 0x03849): (187, "OrderedHashSetMap"),
  ("RO_SPACE", 0x03899): (215, "PreParsedScopeDataMap"),
  ("RO_SPACE", 0x038e9): (216, "PropertyArrayMap"),
  ("RO_SPACE", 0x03939): (209, "SideEffectCallHandlerInfoMap"),
  ("RO_SPACE", 0x03989): (209, "SideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x039d9): (209, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x03a29): (191, "SimpleNumberDictionaryMap"),
  ("RO_SPACE", 0x03a79): (183, "SloppyArgumentsElementsMap"),
  ("RO_SPACE", 0x03ac9): (219, "SmallOrderedHashMapMap"),
  ("RO_SPACE", 0x03b19): (220, "SmallOrderedHashSetMap"),
  ("RO_SPACE", 0x03b69): (192, "StringTableMap"),
  ("RO_SPACE", 0x03bb9): (222, "UncompiledDataWithoutPreParsedScopeMap"),
  ("RO_SPACE", 0x03c09): (223, "UncompiledDataWithPreParsedScopeMap"),
  ("RO_SPACE", 0x03c59): (224, "WeakArrayListMap"),
  ("RO_SPACE", 0x03ca9): (193, "EphemeronHashTableMap"),
  ("RO_SPACE", 0x03cf9): (106, "NativeSourceStringMap"),
  ("RO_SPACE", 0x03d49): (64, "StringMap"),
  ("RO_SPACE", 0x03d99): (73, "ConsOneByteStringMap"),
  ("RO_SPACE", 0x03de9): (65, "ConsStringMap"),
  ("RO_SPACE", 0x03e39): (77, "ThinOneByteStringMap"),
  ("RO_SPACE", 0x03e89): (69, "ThinStringMap"),
  ("RO_SPACE", 0x03ed9): (67, "SlicedStringMap"),
  ("RO_SPACE", 0x03f29): (75, "SlicedOneByteStringMap"),
  ("RO_SPACE", 0x03f79): (66, "ExternalStringMap"),
  ("RO_SPACE", 0x03fc9): (82, "ExternalStringWithOneByteDataMap"),
  ("RO_SPACE", 0x04019): (74, "ExternalOneByteStringMap"),
  ("RO_SPACE", 0x04069): (98, "UncachedExternalStringMap"),
  ("RO_SPACE", 0x040b9): (114, "UncachedExternalStringWithOneByteDataMap"),
  ("RO_SPACE", 0x04109): (0, "InternalizedStringMap"),
  ("RO_SPACE", 0x04159): (2, "ExternalInternalizedStringMap"),
  ("RO_SPACE", 0x041a9): (18, "ExternalInternalizedStringWithOneByteDataMap"),
  ("RO_SPACE", 0x041f9): (10, "ExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x04249): (34, "UncachedExternalInternalizedStringMap"),
  ("RO_SPACE", 0x04299): (50, "UncachedExternalInternalizedStringWithOneByteDataMap"),
  ("RO_SPACE", 0x042e9): (42, "UncachedExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x04339): (106, "UncachedExternalOneByteStringMap"),
  ("RO_SPACE", 0x04389): (140, "FixedUint8ArrayMap"),
  ("RO_SPACE", 0x043d9): (139, "FixedInt8ArrayMap"),
  ("RO_SPACE", 0x04429): (142, "FixedUint16ArrayMap"),
  ("RO_SPACE", 0x04479): (141, "FixedInt16ArrayMap"),
  ("RO_SPACE", 0x044c9): (144, "FixedUint32ArrayMap"),
  ("RO_SPACE", 0x04519): (143, "FixedInt32ArrayMap"),
  ("RO_SPACE", 0x04569): (145, "FixedFloat32ArrayMap"),
  ("RO_SPACE", 0x045b9): (146, "FixedFloat64ArrayMap"),
  ("RO_SPACE", 0x04609): (147, "FixedUint8ClampedArrayMap"),
  ("RO_SPACE", 0x04659): (149, "FixedBigUint64ArrayMap"),
  ("RO_SPACE", 0x046a9): (148, "FixedBigInt64ArrayMap"),
  ("RO_SPACE", 0x046f9): (131, "SelfReferenceMarkerMap"),
  ("RO_SPACE", 0x04761): (171, "Tuple2Map"),
  ("RO_SPACE", 0x04801): (173, "ArrayBoilerplateDescriptionMap"),
  ("RO_SPACE", 0x04b41): (161, "InterceptorInfoMap"),
  ("RO_SPACE", 0x06f49): (153, "AccessCheckInfoMap"),
  ("RO_SPACE", 0x06f99): (154, "AccessorInfoMap"),
  ("RO_SPACE", 0x06fe9): (155, "AccessorPairMap"),
  ("RO_SPACE", 0x07039): (156, "AliasedArgumentsEntryMap"),
  ("RO_SPACE", 0x07089): (157, "AllocationMementoMap"),
  ("RO_SPACE", 0x070d9): (158, "AsyncGeneratorRequestMap"),
  ("RO_SPACE", 0x07129): (159, "DebugInfoMap"),
  ("RO_SPACE", 0x07179): (160, "FunctionTemplateInfoMap"),
  ("RO_SPACE", 0x071c9): (162, "InterpreterDataMap"),
  ("RO_SPACE", 0x07219): (163, "ModuleInfoEntryMap"),
  ("RO_SPACE", 0x07269): (164, "ModuleMap"),
  ("RO_SPACE", 0x072b9): (165, "ObjectTemplateInfoMap"),
  ("RO_SPACE", 0x07309): (166, "PromiseCapabilityMap"),
  ("RO_SPACE", 0x07359): (167, "PromiseReactionMap"),
  ("RO_SPACE", 0x073a9): (168, "PrototypeInfoMap"),
  ("RO_SPACE", 0x073f9): (169, "ScriptMap"),
  ("RO_SPACE", 0x07449): (170, "StackFrameInfoMap"),
  ("RO_SPACE", 0x07499): (172, "Tuple3Map"),
  ("RO_SPACE", 0x074e9): (174, "WasmDebugInfoMap"),
  ("RO_SPACE", 0x07539): (175, "WasmExportedFunctionDataMap"),
  ("RO_SPACE", 0x07589): (176, "CallableTaskMap"),
  ("RO_SPACE", 0x075d9): (177, "CallbackTaskMap"),
  ("RO_SPACE", 0x07629): (178, "PromiseFulfillReactionJobTaskMap"),
  ("RO_SPACE", 0x07679): (179, "PromiseRejectReactionJobTaskMap"),
  ("RO_SPACE", 0x076c9): (180, "PromiseResolveThenableJobTaskMap"),
  ("RO_SPACE", 0x07719): (181, "MicrotaskQueueMap"),
  ("RO_SPACE", 0x07769): (182, "AllocationSiteWithWeakNextMap"),
  ("RO_SPACE", 0x077b9): (182, "AllocationSiteWithoutWeakNextMap"),
  ("RO_SPACE", 0x07809): (214, "LoadHandler1Map"),
  ("RO_SPACE", 0x07859): (214, "LoadHandler2Map"),
  ("RO_SPACE", 0x078a9): (214, "LoadHandler3Map"),
  ("RO_SPACE", 0x078f9): (221, "StoreHandler0Map"),
  ("RO_SPACE", 0x07949): (221, "StoreHandler1Map"),
  ("RO_SPACE", 0x07999): (221, "StoreHandler2Map"),
  ("RO_SPACE", 0x079e9): (221, "StoreHandler3Map"),
  ("MAP_SPACE", 0x02201): (1057, "ExternalMap"),
  ("MAP_SPACE", 0x02251): (1072, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("RO_SPACE", 0x022a1): "NullValue",
  ("RO_SPACE", 0x02321): "EmptyDescriptorArray",
  ("RO_SPACE", 0x02391): "EmptyWeakFixedArray",
  ("RO_SPACE", 0x02491): "UninitializedValue",
  ("RO_SPACE", 0x025a1): "UndefinedValue",
  ("RO_SPACE", 0x02621): "NanValue",
  ("RO_SPACE", 0x02681): "TheHoleValue",
  ("RO_SPACE", 0x02719): "HoleNanValue",
  ("RO_SPACE", 0x02729): "TrueValue",
  ("RO_SPACE", 0x027d9): "FalseValue",
  ("RO_SPACE", 0x02821): "empty_string",
  ("RO_SPACE", 0x02ce1): "EmptyScopeInfo",
  ("RO_SPACE", 0x02cf1): "EmptyFixedArray",
  ("RO_SPACE", 0x02d01): "ArgumentsMarker",
  ("RO_SPACE", 0x02da1): "Exception",
  ("RO_SPACE", 0x02e41): "TerminationException",
  ("RO_SPACE", 0x02ee9): "OptimizedOut",
  ("RO_SPACE", 0x02f89): "StaleRegister",
  ("RO_SPACE", 0x04749): "EmptyEnumCache",
  ("RO_SPACE", 0x047b1): "EmptyPropertyArray",
  ("RO_SPACE", 0x047c1): "EmptyByteArray",
  ("RO_SPACE", 0x047d1): "EmptyObjectBoilerplateDescription",
  ("RO_SPACE", 0x047e9): "EmptyArrayBoilerplateDescription",
  ("RO_SPACE", 0x04851): "EmptyFixedUint8Array",
  ("RO_SPACE", 0x04871): "EmptyFixedInt8Array",
  ("RO_SPACE", 0x04891): "EmptyFixedUint16Array",
  ("RO_SPACE", 0x048b1): "EmptyFixedInt16Array",
  ("RO_SPACE", 0x048d1): "EmptyFixedUint32Array",
  ("RO_SPACE", 0x048f1): "EmptyFixedInt32Array",
  ("RO_SPACE", 0x04911): "EmptyFixedFloat32Array",
  ("RO_SPACE", 0x04931): "EmptyFixedFloat64Array",
  ("RO_SPACE", 0x04951): "EmptyFixedUint8ClampedArray",
  ("RO_SPACE", 0x04971): "EmptyFixedBigUint64Array",
  ("RO_SPACE", 0x04991): "EmptyFixedBigInt64Array",
  ("RO_SPACE", 0x049b1): "EmptySloppyArgumentsElements",
  ("RO_SPACE", 0x049d1): "EmptySlowElementDictionary",
  ("RO_SPACE", 0x04a19): "EmptyOrderedHashMap",
  ("RO_SPACE", 0x04a41): "EmptyOrderedHashSet",
  ("RO_SPACE", 0x04a69): "EmptyFeedbackMetadata",
  ("RO_SPACE", 0x04a79): "EmptyPropertyCell",
  ("RO_SPACE", 0x04aa1): "EmptyPropertyDictionary",
  ("RO_SPACE", 0x04af1): "NoOpInterceptorInfo",
  ("RO_SPACE", 0x04b91): "EmptyWeakArrayList",
  ("RO_SPACE", 0x04ba9): "InfinityValue",
  ("RO_SPACE", 0x04bb9): "MinusZeroValue",
  ("RO_SPACE", 0x04bc9): "MinusInfinityValue",
  ("RO_SPACE", 0x04bd9): "SelfReferenceMarker",
  ("OLD_SPACE", 0x02201): "ArgumentsIteratorAccessor",
  ("OLD_SPACE", 0x02271): "ArrayLengthAccessor",
  ("OLD_SPACE", 0x022e1): "BoundFunctionLengthAccessor",
  ("OLD_SPACE", 0x02351): "BoundFunctionNameAccessor",
  ("OLD_SPACE", 0x023c1): "ErrorStackAccessor",
  ("OLD_SPACE", 0x02431): "FunctionArgumentsAccessor",
  ("OLD_SPACE", 0x024a1): "FunctionCallerAccessor",
  ("OLD_SPACE", 0x02511): "FunctionNameAccessor",
  ("OLD_SPACE", 0x02581): "FunctionLengthAccessor",
  ("OLD_SPACE", 0x025f1): "FunctionPrototypeAccessor",
  ("OLD_SPACE", 0x02661): "StringLengthAccessor",
  ("OLD_SPACE", 0x026d1): "InvalidPrototypeValidityCell",
  ("OLD_SPACE", 0x026e1): "EmptyScript",
  ("OLD_SPACE", 0x02761): "ManyClosuresCell",
  ("OLD_SPACE", 0x02771): "ArrayConstructorProtector",
  ("OLD_SPACE", 0x02781): "NoElementsProtector",
  ("OLD_SPACE", 0x027a9): "IsConcatSpreadableProtector",
  ("OLD_SPACE", 0x027b9): "ArraySpeciesProtector",
  ("OLD_SPACE", 0x027e1): "TypedArraySpeciesProtector",
  ("OLD_SPACE", 0x02809): "PromiseSpeciesProtector",
  ("OLD_SPACE", 0x02831): "StringLengthProtector",
  ("OLD_SPACE", 0x02841): "ArrayIteratorProtector",
  ("OLD_SPACE", 0x02869): "ArrayBufferNeuteringProtector",
  ("OLD_SPACE", 0x02891): "PromiseHookProtector",
  ("OLD_SPACE", 0x028b9): "PromiseResolveProtector",
  ("OLD_SPACE", 0x028c9): "PromiseThenProtector",
  ("OLD_SPACE", 0x028f1): "StringIteratorProtector",
  ("OLD_SPACE", 0x02919): "SingleCharacterStringCache",
  ("OLD_SPACE", 0x03129): "StringSplitCache",
  ("OLD_SPACE", 0x03939): "RegExpMultipleCache",
  ("OLD_SPACE", 0x04149): "DefaultMicrotaskQueue",
  ("OLD_SPACE", 0x04161): "BuiltinsConstantsTable",
  ("OLD_SPACE", 0x04a71): "HashSeed",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
