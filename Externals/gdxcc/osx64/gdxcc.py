# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.5
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gdxcc', [dirname(__file__)])
        except ImportError:
            import _gdxcc
            return _gdxcc
        if fp is not None:
            try:
                _mod = imp.load_module('_gdxcc', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _gdxcc = swig_import_helper()
    del swig_import_helper
else:
    import _gdxcc
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class intArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _gdxcc.new_intArray(nelements)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _gdxcc.delete_intArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _gdxcc.intArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _gdxcc.intArray___setitem__(self, index, value)

    def cast(self):
        return _gdxcc.intArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _gdxcc.intArray_frompointer
    if _newclass:
        frompointer = staticmethod(_gdxcc.intArray_frompointer)
intArray_swigregister = _gdxcc.intArray_swigregister
intArray_swigregister(intArray)

def intArray_frompointer(t):
    return _gdxcc.intArray_frompointer(t)
intArray_frompointer = _gdxcc.intArray_frompointer

class doubleArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doubleArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doubleArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _gdxcc.new_doubleArray(nelements)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _gdxcc.delete_doubleArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _gdxcc.doubleArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _gdxcc.doubleArray___setitem__(self, index, value)

    def cast(self):
        return _gdxcc.doubleArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _gdxcc.doubleArray_frompointer
    if _newclass:
        frompointer = staticmethod(_gdxcc.doubleArray_frompointer)
doubleArray_swigregister = _gdxcc.doubleArray_swigregister
doubleArray_swigregister(doubleArray)

def doubleArray_frompointer(t):
    return _gdxcc.doubleArray_frompointer(t)
doubleArray_frompointer = _gdxcc.doubleArray_frompointer


def new_intp():
    return _gdxcc.new_intp()
new_intp = _gdxcc.new_intp

def copy_intp(value):
    return _gdxcc.copy_intp(value)
copy_intp = _gdxcc.copy_intp

def delete_intp(obj):
    return _gdxcc.delete_intp(obj)
delete_intp = _gdxcc.delete_intp

def intp_assign(obj, value):
    return _gdxcc.intp_assign(obj, value)
intp_assign = _gdxcc.intp_assign

def intp_value(obj):
    return _gdxcc.intp_value(obj)
intp_value = _gdxcc.intp_value

def new_doublep():
    return _gdxcc.new_doublep()
new_doublep = _gdxcc.new_doublep

def copy_doublep(value):
    return _gdxcc.copy_doublep(value)
copy_doublep = _gdxcc.copy_doublep

def delete_doublep(obj):
    return _gdxcc.delete_doublep(obj)
delete_doublep = _gdxcc.delete_doublep

def doublep_assign(obj, value):
    return _gdxcc.doublep_assign(obj, value)
doublep_assign = _gdxcc.doublep_assign

def doublep_value(obj):
    return _gdxcc.doublep_value(obj)
doublep_value = _gdxcc.doublep_value

def new_gdxHandle_tp():
    return _gdxcc.new_gdxHandle_tp()
new_gdxHandle_tp = _gdxcc.new_gdxHandle_tp

def copy_gdxHandle_tp(value):
    return _gdxcc.copy_gdxHandle_tp(value)
copy_gdxHandle_tp = _gdxcc.copy_gdxHandle_tp

def delete_gdxHandle_tp(obj):
    return _gdxcc.delete_gdxHandle_tp(obj)
delete_gdxHandle_tp = _gdxcc.delete_gdxHandle_tp

def gdxHandle_tp_assign(obj, value):
    return _gdxcc.gdxHandle_tp_assign(obj, value)
gdxHandle_tp_assign = _gdxcc.gdxHandle_tp_assign

def gdxHandle_tp_value(obj):
    return _gdxcc.gdxHandle_tp_value(obj)
gdxHandle_tp_value = _gdxcc.gdxHandle_tp_value

def new_TDataStoreProc_tp():
    return _gdxcc.new_TDataStoreProc_tp()
new_TDataStoreProc_tp = _gdxcc.new_TDataStoreProc_tp

def copy_TDataStoreProc_tp(value):
    return _gdxcc.copy_TDataStoreProc_tp(value)
copy_TDataStoreProc_tp = _gdxcc.copy_TDataStoreProc_tp

def delete_TDataStoreProc_tp(obj):
    return _gdxcc.delete_TDataStoreProc_tp(obj)
delete_TDataStoreProc_tp = _gdxcc.delete_TDataStoreProc_tp

def TDataStoreProc_tp_assign(obj, value):
    return _gdxcc.TDataStoreProc_tp_assign(obj, value)
TDataStoreProc_tp_assign = _gdxcc.TDataStoreProc_tp_assign

def TDataStoreProc_tp_value(obj):
    return _gdxcc.TDataStoreProc_tp_value(obj)
TDataStoreProc_tp_value = _gdxcc.TDataStoreProc_tp_value

def new_TDataStoreFiltProc_tp():
    return _gdxcc.new_TDataStoreFiltProc_tp()
new_TDataStoreFiltProc_tp = _gdxcc.new_TDataStoreFiltProc_tp

def copy_TDataStoreFiltProc_tp(value):
    return _gdxcc.copy_TDataStoreFiltProc_tp(value)
copy_TDataStoreFiltProc_tp = _gdxcc.copy_TDataStoreFiltProc_tp

def delete_TDataStoreFiltProc_tp(obj):
    return _gdxcc.delete_TDataStoreFiltProc_tp(obj)
delete_TDataStoreFiltProc_tp = _gdxcc.delete_TDataStoreFiltProc_tp

def TDataStoreFiltProc_tp_assign(obj, value):
    return _gdxcc.TDataStoreFiltProc_tp_assign(obj, value)
TDataStoreFiltProc_tp_assign = _gdxcc.TDataStoreFiltProc_tp_assign

def TDataStoreFiltProc_tp_value(obj):
    return _gdxcc.TDataStoreFiltProc_tp_value(obj)
TDataStoreFiltProc_tp_value = _gdxcc.TDataStoreFiltProc_tp_value

def new_TDomainIndexProc_tp():
    return _gdxcc.new_TDomainIndexProc_tp()
new_TDomainIndexProc_tp = _gdxcc.new_TDomainIndexProc_tp

def copy_TDomainIndexProc_tp(value):
    return _gdxcc.copy_TDomainIndexProc_tp(value)
copy_TDomainIndexProc_tp = _gdxcc.copy_TDomainIndexProc_tp

def delete_TDomainIndexProc_tp(obj):
    return _gdxcc.delete_TDomainIndexProc_tp(obj)
delete_TDomainIndexProc_tp = _gdxcc.delete_TDomainIndexProc_tp

def TDomainIndexProc_tp_assign(obj, value):
    return _gdxcc.TDomainIndexProc_tp_assign(obj, value)
TDomainIndexProc_tp_assign = _gdxcc.TDomainIndexProc_tp_assign

def TDomainIndexProc_tp_value(obj):
    return _gdxcc.TDomainIndexProc_tp_value(obj)
TDomainIndexProc_tp_value = _gdxcc.TDomainIndexProc_tp_value

def gdxHandleToPtr(pgdx):
    """gdxHandleToPtr(pgdx) -> void *"""
    return _gdxcc.gdxHandleToPtr(pgdx)

def ptrTogdxHandle(vptr):
    """ptrTogdxHandle(vptr) -> gdxHandle_t"""
    return _gdxcc.ptrTogdxHandle(vptr)

def gdxGetReady(msgBufSize):
    """gdxGetReady(msgBufSize) -> int"""
    return _gdxcc.gdxGetReady(msgBufSize)

def gdxGetReadyD(dirName, msgBufSize):
    """gdxGetReadyD(dirName, msgBufSize) -> int"""
    return _gdxcc.gdxGetReadyD(dirName, msgBufSize)

def gdxGetReadyL(libName, msgBufSize):
    """gdxGetReadyL(libName, msgBufSize) -> int"""
    return _gdxcc.gdxGetReadyL(libName, msgBufSize)

def gdxCreate(pgdx, msgBufSize):
    """gdxCreate(pgdx, msgBufSize) -> int"""
    return _gdxcc.gdxCreate(pgdx, msgBufSize)

def gdxCreateD(pgdx, dirName, msgBufSize):
    """gdxCreateD(pgdx, dirName, msgBufSize) -> int"""
    return _gdxcc.gdxCreateD(pgdx, dirName, msgBufSize)

def gdxCreateL(pgdx, libName, msgBufSize):
    """gdxCreateL(pgdx, libName, msgBufSize) -> int"""
    return _gdxcc.gdxCreateL(pgdx, libName, msgBufSize)

def gdxFree(pgdx):
    """gdxFree(pgdx) -> int"""
    return _gdxcc.gdxFree(pgdx)

def gdxLibraryLoaded():
    """gdxLibraryLoaded() -> int"""
    return _gdxcc.gdxLibraryLoaded()

def gdxLibraryUnload():
    """gdxLibraryUnload() -> int"""
    return _gdxcc.gdxLibraryUnload()

def gdxGetScreenIndicator():
    """gdxGetScreenIndicator() -> int"""
    return _gdxcc.gdxGetScreenIndicator()

def gdxSetScreenIndicator(scrind):
    """gdxSetScreenIndicator(scrind)"""
    return _gdxcc.gdxSetScreenIndicator(scrind)

def gdxGetExceptionIndicator():
    """gdxGetExceptionIndicator() -> int"""
    return _gdxcc.gdxGetExceptionIndicator()

def gdxSetExceptionIndicator(excind):
    """gdxSetExceptionIndicator(excind)"""
    return _gdxcc.gdxSetExceptionIndicator(excind)

def gdxGetExitIndicator():
    """gdxGetExitIndicator() -> int"""
    return _gdxcc.gdxGetExitIndicator()

def gdxSetExitIndicator(extind):
    """gdxSetExitIndicator(extind)"""
    return _gdxcc.gdxSetExitIndicator(extind)

def gdxGetErrorCallback():
    """gdxGetErrorCallback() -> gdxErrorCallback_t"""
    return _gdxcc.gdxGetErrorCallback()

def gdxSetErrorCallback(func):
    """gdxSetErrorCallback(func)"""
    return _gdxcc.gdxSetErrorCallback(func)

def gdxGetAPIErrorCount():
    """gdxGetAPIErrorCount() -> int"""
    return _gdxcc.gdxGetAPIErrorCount()

def gdxSetAPIErrorCount(ecnt):
    """gdxSetAPIErrorCount(ecnt)"""
    return _gdxcc.gdxSetAPIErrorCount(ecnt)

def gdxErrorHandling(msg):
    """gdxErrorHandling(msg)"""
    return _gdxcc.gdxErrorHandling(msg)

def gdxAcronymAdd(pgdx, AName, Txt, AIndx):
    """gdxAcronymAdd(pgdx, AName, Txt, AIndx) -> int"""
    return _gdxcc.gdxAcronymAdd(pgdx, AName, Txt, AIndx)

def gdxAcronymCount(pgdx):
    """gdxAcronymCount(pgdx) -> int"""
    return _gdxcc.gdxAcronymCount(pgdx)

def gdxAcronymGetInfo(pgdx, N):
    """gdxAcronymGetInfo(pgdx, N) -> int"""
    return _gdxcc.gdxAcronymGetInfo(pgdx, N)

def gdxAcronymGetMapping(pgdx, N):
    """gdxAcronymGetMapping(pgdx, N) -> int"""
    return _gdxcc.gdxAcronymGetMapping(pgdx, N)

def gdxAcronymIndex(pgdx, V):
    """gdxAcronymIndex(pgdx, V) -> int"""
    return _gdxcc.gdxAcronymIndex(pgdx, V)

def gdxAcronymName(pgdx, V):
    """gdxAcronymName(pgdx, V) -> int"""
    return _gdxcc.gdxAcronymName(pgdx, V)

def gdxAcronymNextNr(pgdx, NV):
    """gdxAcronymNextNr(pgdx, NV) -> int"""
    return _gdxcc.gdxAcronymNextNr(pgdx, NV)

def gdxAcronymSetInfo(pgdx, N, AName, Txt, AIndx):
    """gdxAcronymSetInfo(pgdx, N, AName, Txt, AIndx) -> int"""
    return _gdxcc.gdxAcronymSetInfo(pgdx, N, AName, Txt, AIndx)

def gdxAcronymValue(pgdx, AIndx):
    """gdxAcronymValue(pgdx, AIndx) -> double"""
    return _gdxcc.gdxAcronymValue(pgdx, AIndx)

def gdxAddAlias(pgdx, Id1, Id2):
    """gdxAddAlias(pgdx, Id1, Id2) -> int"""
    return _gdxcc.gdxAddAlias(pgdx, Id1, Id2)

def gdxAddSetText(pgdx, Txt):
    """gdxAddSetText(pgdx, Txt) -> int"""
    return _gdxcc.gdxAddSetText(pgdx, Txt)

def gdxAutoConvert(pgdx, NV):
    """gdxAutoConvert(pgdx, NV) -> int"""
    return _gdxcc.gdxAutoConvert(pgdx, NV)

def gdxClose(pgdx):
    """gdxClose(pgdx) -> int"""
    return _gdxcc.gdxClose(pgdx)

def gdxDataErrorCount(pgdx):
    """gdxDataErrorCount(pgdx) -> int"""
    return _gdxcc.gdxDataErrorCount(pgdx)

def gdxDataErrorRecord(pgdx, RecNr):
    """gdxDataErrorRecord(pgdx, RecNr) -> int"""
    return _gdxcc.gdxDataErrorRecord(pgdx, RecNr)

def gdxDataErrorRecordX(pgdx, RecNr):
    """gdxDataErrorRecordX(pgdx, RecNr) -> int"""
    return _gdxcc.gdxDataErrorRecordX(pgdx, RecNr)

def gdxDataReadDone(pgdx):
    """gdxDataReadDone(pgdx) -> int"""
    return _gdxcc.gdxDataReadDone(pgdx)

def gdxDataReadFilteredStart(pgdx, SyNr, FilterAction):
    """gdxDataReadFilteredStart(pgdx, SyNr, FilterAction) -> int"""
    return _gdxcc.gdxDataReadFilteredStart(pgdx, SyNr, FilterAction)

def gdxDataReadMap(pgdx, RecNr):
    """gdxDataReadMap(pgdx, RecNr) -> int"""
    return _gdxcc.gdxDataReadMap(pgdx, RecNr)

def gdxDataReadMapStart(pgdx, SyNr):
    """gdxDataReadMapStart(pgdx, SyNr) -> int"""
    return _gdxcc.gdxDataReadMapStart(pgdx, SyNr)

def gdxDataReadRaw(pgdx):
    """gdxDataReadRaw(pgdx) -> int"""
    return _gdxcc.gdxDataReadRaw(pgdx)

def gdxDataReadRawFast(pgdx, SyNr, DP):
    """gdxDataReadRawFast(pgdx, SyNr, DP) -> int"""
    return _gdxcc.gdxDataReadRawFast(pgdx, SyNr, DP)

def gdxDataReadRawFastFilt(pgdx, SyNr, UelFilterStr_in, DP):
    """gdxDataReadRawFastFilt(pgdx, SyNr, UelFilterStr_in, DP) -> int"""
    return _gdxcc.gdxDataReadRawFastFilt(pgdx, SyNr, UelFilterStr_in, DP)

def gdxDataReadRawStart(pgdx, SyNr):
    """gdxDataReadRawStart(pgdx, SyNr) -> int"""
    return _gdxcc.gdxDataReadRawStart(pgdx, SyNr)

def gdxDataReadSlice(pgdx, UelFilterStr_in, DP):
    """gdxDataReadSlice(pgdx, UelFilterStr_in, DP) -> int"""
    return _gdxcc.gdxDataReadSlice(pgdx, UelFilterStr_in, DP)

def gdxDataReadSliceStart(pgdx, SyNr):
    """gdxDataReadSliceStart(pgdx, SyNr) -> int"""
    return _gdxcc.gdxDataReadSliceStart(pgdx, SyNr)

def gdxDataReadStr(pgdx):
    """gdxDataReadStr(pgdx) -> int"""
    return _gdxcc.gdxDataReadStr(pgdx)

def gdxDataReadStrStart(pgdx, SyNr):
    """gdxDataReadStrStart(pgdx, SyNr) -> int"""
    return _gdxcc.gdxDataReadStrStart(pgdx, SyNr)

def gdxDataSliceUELS(pgdx, SliceKeyInt):
    """gdxDataSliceUELS(pgdx, SliceKeyInt) -> int"""
    return _gdxcc.gdxDataSliceUELS(pgdx, SliceKeyInt)

def gdxDataWriteDone(pgdx):
    """gdxDataWriteDone(pgdx) -> int"""
    return _gdxcc.gdxDataWriteDone(pgdx)

def gdxDataWriteMap(pgdx, KeyInt, Values):
    """gdxDataWriteMap(pgdx, KeyInt, Values) -> int"""
    return _gdxcc.gdxDataWriteMap(pgdx, KeyInt, Values)

def gdxDataWriteMapStart(pgdx, SyId, ExplTxt, Dimen, Typ, UserInfo):
    """gdxDataWriteMapStart(pgdx, SyId, ExplTxt, Dimen, Typ, UserInfo) -> int"""
    return _gdxcc.gdxDataWriteMapStart(pgdx, SyId, ExplTxt, Dimen, Typ, UserInfo)

def gdxDataWriteRaw(pgdx, KeyInt, Values):
    """gdxDataWriteRaw(pgdx, KeyInt, Values) -> int"""
    return _gdxcc.gdxDataWriteRaw(pgdx, KeyInt, Values)

def gdxDataWriteRawStart(pgdx, SyId, ExplTxt, Dimen, Typ, UserInfo):
    """gdxDataWriteRawStart(pgdx, SyId, ExplTxt, Dimen, Typ, UserInfo) -> int"""
    return _gdxcc.gdxDataWriteRawStart(pgdx, SyId, ExplTxt, Dimen, Typ, UserInfo)

def gdxDataWriteStr(pgdx, KeyStr_in, Values):
    """gdxDataWriteStr(pgdx, KeyStr_in, Values) -> int"""
    return _gdxcc.gdxDataWriteStr(pgdx, KeyStr_in, Values)

def gdxDataWriteStrStart(pgdx, SyId, ExplTxt, Dimen, Typ, UserInfo):
    """gdxDataWriteStrStart(pgdx, SyId, ExplTxt, Dimen, Typ, UserInfo) -> int"""
    return _gdxcc.gdxDataWriteStrStart(pgdx, SyId, ExplTxt, Dimen, Typ, UserInfo)

def gdxGetDLLVersion(pgdx):
    """gdxGetDLLVersion(pgdx) -> int"""
    return _gdxcc.gdxGetDLLVersion(pgdx)

def gdxErrorCount(pgdx):
    """gdxErrorCount(pgdx) -> int"""
    return _gdxcc.gdxErrorCount(pgdx)

def gdxErrorStr(pgdx, ErrNr):
    """gdxErrorStr(pgdx, ErrNr) -> int"""
    return _gdxcc.gdxErrorStr(pgdx, ErrNr)

def gdxFileInfo(pgdx):
    """gdxFileInfo(pgdx) -> int"""
    return _gdxcc.gdxFileInfo(pgdx)

def gdxFileVersion(pgdx):
    """gdxFileVersion(pgdx) -> int"""
    return _gdxcc.gdxFileVersion(pgdx)

def gdxFilterExists(pgdx, FilterNr):
    """gdxFilterExists(pgdx, FilterNr) -> int"""
    return _gdxcc.gdxFilterExists(pgdx, FilterNr)

def gdxFilterRegister(pgdx, UelMap):
    """gdxFilterRegister(pgdx, UelMap) -> int"""
    return _gdxcc.gdxFilterRegister(pgdx, UelMap)

def gdxFilterRegisterDone(pgdx):
    """gdxFilterRegisterDone(pgdx) -> int"""
    return _gdxcc.gdxFilterRegisterDone(pgdx)

def gdxFilterRegisterStart(pgdx, FilterNr):
    """gdxFilterRegisterStart(pgdx, FilterNr) -> int"""
    return _gdxcc.gdxFilterRegisterStart(pgdx, FilterNr)

def gdxFindSymbol(pgdx, SyId):
    """gdxFindSymbol(pgdx, SyId) -> int"""
    return _gdxcc.gdxFindSymbol(pgdx, SyId)

def gdxGetElemText(pgdx, TxtNr):
    """gdxGetElemText(pgdx, TxtNr) -> int"""
    return _gdxcc.gdxGetElemText(pgdx, TxtNr)

def gdxGetLastError(pgdx):
    """gdxGetLastError(pgdx) -> int"""
    return _gdxcc.gdxGetLastError(pgdx)

def gdxGetMemoryUsed(pgdx):
    """gdxGetMemoryUsed(pgdx) -> INT64"""
    return _gdxcc.gdxGetMemoryUsed(pgdx)

def gdxGetSpecialValues(pgdx, AVals):
    """gdxGetSpecialValues(pgdx, AVals) -> int"""
    return _gdxcc.gdxGetSpecialValues(pgdx, AVals)

def gdxGetUEL(pgdx, UelNr):
    """gdxGetUEL(pgdx, UelNr) -> int"""
    return _gdxcc.gdxGetUEL(pgdx, UelNr)

def gdxMapValue(pgdx, D):
    """gdxMapValue(pgdx, D) -> int"""
    return _gdxcc.gdxMapValue(pgdx, D)

def gdxOpenAppend(pgdx, FileName, Producer):
    """gdxOpenAppend(pgdx, FileName, Producer) -> int"""
    return _gdxcc.gdxOpenAppend(pgdx, FileName, Producer)

def gdxOpenRead(pgdx, FileName):
    """gdxOpenRead(pgdx, FileName) -> int"""
    return _gdxcc.gdxOpenRead(pgdx, FileName)

def gdxOpenWrite(pgdx, FileName, Producer):
    """gdxOpenWrite(pgdx, FileName, Producer) -> int"""
    return _gdxcc.gdxOpenWrite(pgdx, FileName, Producer)

def gdxOpenWriteEx(pgdx, FileName, Producer, Compr):
    """gdxOpenWriteEx(pgdx, FileName, Producer, Compr) -> int"""
    return _gdxcc.gdxOpenWriteEx(pgdx, FileName, Producer, Compr)

def gdxResetSpecialValues(pgdx):
    """gdxResetSpecialValues(pgdx) -> int"""
    return _gdxcc.gdxResetSpecialValues(pgdx)

def gdxSetHasText(pgdx, SyNr):
    """gdxSetHasText(pgdx, SyNr) -> int"""
    return _gdxcc.gdxSetHasText(pgdx, SyNr)

def gdxSetReadSpecialValues(pgdx, AVals):
    """gdxSetReadSpecialValues(pgdx, AVals) -> int"""
    return _gdxcc.gdxSetReadSpecialValues(pgdx, AVals)

def gdxSetSpecialValues(pgdx, AVals):
    """gdxSetSpecialValues(pgdx, AVals) -> int"""
    return _gdxcc.gdxSetSpecialValues(pgdx, AVals)

def gdxSetTextNodeNr(pgdx, TxtNr, Node):
    """gdxSetTextNodeNr(pgdx, TxtNr, Node) -> int"""
    return _gdxcc.gdxSetTextNodeNr(pgdx, TxtNr, Node)

def gdxSetTraceLevel(pgdx, N, s):
    """gdxSetTraceLevel(pgdx, N, s) -> int"""
    return _gdxcc.gdxSetTraceLevel(pgdx, N, s)

def gdxSymbIndxMaxLength(pgdx, SyNr):
    """gdxSymbIndxMaxLength(pgdx, SyNr) -> int"""
    return _gdxcc.gdxSymbIndxMaxLength(pgdx, SyNr)

def gdxSymbMaxLength(pgdx):
    """gdxSymbMaxLength(pgdx) -> int"""
    return _gdxcc.gdxSymbMaxLength(pgdx)

def gdxSymbolAddComment(pgdx, SyNr, Txt):
    """gdxSymbolAddComment(pgdx, SyNr, Txt) -> int"""
    return _gdxcc.gdxSymbolAddComment(pgdx, SyNr, Txt)

def gdxSymbolGetComment(pgdx, SyNr, N):
    """gdxSymbolGetComment(pgdx, SyNr, N) -> int"""
    return _gdxcc.gdxSymbolGetComment(pgdx, SyNr, N)

def gdxSymbolGetDomain(pgdx, SyNr):
    """gdxSymbolGetDomain(pgdx, SyNr) -> int"""
    return _gdxcc.gdxSymbolGetDomain(pgdx, SyNr)

def gdxSymbolGetDomainX(pgdx, SyNr):
    """gdxSymbolGetDomainX(pgdx, SyNr) -> int"""
    return _gdxcc.gdxSymbolGetDomainX(pgdx, SyNr)

def gdxSymbolDim(pgdx, SyNr):
    """gdxSymbolDim(pgdx, SyNr) -> int"""
    return _gdxcc.gdxSymbolDim(pgdx, SyNr)

def gdxSymbolInfo(pgdx, SyNr):
    """gdxSymbolInfo(pgdx, SyNr) -> int"""
    return _gdxcc.gdxSymbolInfo(pgdx, SyNr)

def gdxSymbolInfoX(pgdx, SyNr):
    """gdxSymbolInfoX(pgdx, SyNr) -> int"""
    return _gdxcc.gdxSymbolInfoX(pgdx, SyNr)

def gdxSymbolSetDomain(pgdx, DomainIDs_in):
    """gdxSymbolSetDomain(pgdx, DomainIDs_in) -> int"""
    return _gdxcc.gdxSymbolSetDomain(pgdx, DomainIDs_in)

def gdxSymbolSetDomainX(pgdx, SyNr, DomainIDs_in):
    """gdxSymbolSetDomainX(pgdx, SyNr, DomainIDs_in) -> int"""
    return _gdxcc.gdxSymbolSetDomainX(pgdx, SyNr, DomainIDs_in)

def gdxSystemInfo(pgdx):
    """gdxSystemInfo(pgdx) -> int"""
    return _gdxcc.gdxSystemInfo(pgdx)

def gdxUELMaxLength(pgdx):
    """gdxUELMaxLength(pgdx) -> int"""
    return _gdxcc.gdxUELMaxLength(pgdx)

def gdxUELRegisterDone(pgdx):
    """gdxUELRegisterDone(pgdx) -> int"""
    return _gdxcc.gdxUELRegisterDone(pgdx)

def gdxUELRegisterMap(pgdx, UMap, Uel):
    """gdxUELRegisterMap(pgdx, UMap, Uel) -> int"""
    return _gdxcc.gdxUELRegisterMap(pgdx, UMap, Uel)

def gdxUELRegisterMapStart(pgdx):
    """gdxUELRegisterMapStart(pgdx) -> int"""
    return _gdxcc.gdxUELRegisterMapStart(pgdx)

def gdxUELRegisterRaw(pgdx, Uel):
    """gdxUELRegisterRaw(pgdx, Uel) -> int"""
    return _gdxcc.gdxUELRegisterRaw(pgdx, Uel)

def gdxUELRegisterRawStart(pgdx):
    """gdxUELRegisterRawStart(pgdx) -> int"""
    return _gdxcc.gdxUELRegisterRawStart(pgdx)

def gdxUELRegisterStr(pgdx, Uel):
    """gdxUELRegisterStr(pgdx, Uel) -> int"""
    return _gdxcc.gdxUELRegisterStr(pgdx, Uel)

def gdxUELRegisterStrStart(pgdx):
    """gdxUELRegisterStrStart(pgdx) -> int"""
    return _gdxcc.gdxUELRegisterStrStart(pgdx)

def gdxUMFindUEL(pgdx, Uel):
    """gdxUMFindUEL(pgdx, Uel) -> int"""
    return _gdxcc.gdxUMFindUEL(pgdx, Uel)

def gdxUMUelGet(pgdx, UelNr):
    """gdxUMUelGet(pgdx, UelNr) -> int"""
    return _gdxcc.gdxUMUelGet(pgdx, UelNr)

def gdxUMUelInfo(pgdx):
    """gdxUMUelInfo(pgdx) -> int"""
    return _gdxcc.gdxUMUelInfo(pgdx)

def gdxGetDomainElements(pgdx, SyNr, DimPos, FilterNr, DP, Uptr):
    """gdxGetDomainElements(pgdx, SyNr, DimPos, FilterNr, DP, Uptr) -> int"""
    return _gdxcc.gdxGetDomainElements(pgdx, SyNr, DimPos, FilterNr, DP, Uptr)

def gdxCurrentDim(pgdx):
    """gdxCurrentDim(pgdx) -> int"""
    return _gdxcc.gdxCurrentDim(pgdx)

def gdxRenameUEL(pgdx, OldName, NewName):
    """gdxRenameUEL(pgdx, OldName, NewName) -> int"""
    return _gdxcc.gdxRenameUEL(pgdx, OldName, NewName)

_gdxcc.GLOBAL_MAX_INDEX_DIM_swigconstant(_gdxcc)
GLOBAL_MAX_INDEX_DIM = _gdxcc.GLOBAL_MAX_INDEX_DIM

_gdxcc.GLOBAL_UEL_IDENT_SIZE_swigconstant(_gdxcc)
GLOBAL_UEL_IDENT_SIZE = _gdxcc.GLOBAL_UEL_IDENT_SIZE

_gdxcc.ITERLIM_INFINITY_swigconstant(_gdxcc)
ITERLIM_INFINITY = _gdxcc.ITERLIM_INFINITY

_gdxcc.GMS_MAX_INDEX_DIM_swigconstant(_gdxcc)
GMS_MAX_INDEX_DIM = _gdxcc.GMS_MAX_INDEX_DIM

_gdxcc.GMS_UEL_IDENT_SIZE_swigconstant(_gdxcc)
GMS_UEL_IDENT_SIZE = _gdxcc.GMS_UEL_IDENT_SIZE

_gdxcc.GMS_SSSIZE_swigconstant(_gdxcc)
GMS_SSSIZE = _gdxcc.GMS_SSSIZE

_gdxcc.GMS_VARTYPE_UNKNOWN_swigconstant(_gdxcc)
GMS_VARTYPE_UNKNOWN = _gdxcc.GMS_VARTYPE_UNKNOWN

_gdxcc.GMS_VARTYPE_BINARY_swigconstant(_gdxcc)
GMS_VARTYPE_BINARY = _gdxcc.GMS_VARTYPE_BINARY

_gdxcc.GMS_VARTYPE_INTEGER_swigconstant(_gdxcc)
GMS_VARTYPE_INTEGER = _gdxcc.GMS_VARTYPE_INTEGER

_gdxcc.GMS_VARTYPE_POSITIVE_swigconstant(_gdxcc)
GMS_VARTYPE_POSITIVE = _gdxcc.GMS_VARTYPE_POSITIVE

_gdxcc.GMS_VARTYPE_NEGATIVE_swigconstant(_gdxcc)
GMS_VARTYPE_NEGATIVE = _gdxcc.GMS_VARTYPE_NEGATIVE

_gdxcc.GMS_VARTYPE_FREE_swigconstant(_gdxcc)
GMS_VARTYPE_FREE = _gdxcc.GMS_VARTYPE_FREE

_gdxcc.GMS_VARTYPE_SOS1_swigconstant(_gdxcc)
GMS_VARTYPE_SOS1 = _gdxcc.GMS_VARTYPE_SOS1

_gdxcc.GMS_VARTYPE_SOS2_swigconstant(_gdxcc)
GMS_VARTYPE_SOS2 = _gdxcc.GMS_VARTYPE_SOS2

_gdxcc.GMS_VARTYPE_SEMICONT_swigconstant(_gdxcc)
GMS_VARTYPE_SEMICONT = _gdxcc.GMS_VARTYPE_SEMICONT

_gdxcc.GMS_VARTYPE_SEMIINT_swigconstant(_gdxcc)
GMS_VARTYPE_SEMIINT = _gdxcc.GMS_VARTYPE_SEMIINT

_gdxcc.GMS_VARTYPE_MAX_swigconstant(_gdxcc)
GMS_VARTYPE_MAX = _gdxcc.GMS_VARTYPE_MAX

_gdxcc.GMS_EQUTYPE_E_swigconstant(_gdxcc)
GMS_EQUTYPE_E = _gdxcc.GMS_EQUTYPE_E

_gdxcc.GMS_EQUTYPE_G_swigconstant(_gdxcc)
GMS_EQUTYPE_G = _gdxcc.GMS_EQUTYPE_G

_gdxcc.GMS_EQUTYPE_L_swigconstant(_gdxcc)
GMS_EQUTYPE_L = _gdxcc.GMS_EQUTYPE_L

_gdxcc.GMS_EQUTYPE_N_swigconstant(_gdxcc)
GMS_EQUTYPE_N = _gdxcc.GMS_EQUTYPE_N

_gdxcc.GMS_EQUTYPE_X_swigconstant(_gdxcc)
GMS_EQUTYPE_X = _gdxcc.GMS_EQUTYPE_X

_gdxcc.GMS_EQUTYPE_C_swigconstant(_gdxcc)
GMS_EQUTYPE_C = _gdxcc.GMS_EQUTYPE_C

_gdxcc.GMS_EQUTYPE_MAX_swigconstant(_gdxcc)
GMS_EQUTYPE_MAX = _gdxcc.GMS_EQUTYPE_MAX

_gdxcc.GMS_VAL_LEVEL_swigconstant(_gdxcc)
GMS_VAL_LEVEL = _gdxcc.GMS_VAL_LEVEL

_gdxcc.GMS_VAL_MARGINAL_swigconstant(_gdxcc)
GMS_VAL_MARGINAL = _gdxcc.GMS_VAL_MARGINAL

_gdxcc.GMS_VAL_LOWER_swigconstant(_gdxcc)
GMS_VAL_LOWER = _gdxcc.GMS_VAL_LOWER

_gdxcc.GMS_VAL_UPPER_swigconstant(_gdxcc)
GMS_VAL_UPPER = _gdxcc.GMS_VAL_UPPER

_gdxcc.GMS_VAL_SCALE_swigconstant(_gdxcc)
GMS_VAL_SCALE = _gdxcc.GMS_VAL_SCALE

_gdxcc.GMS_VAL_MAX_swigconstant(_gdxcc)
GMS_VAL_MAX = _gdxcc.GMS_VAL_MAX

_gdxcc.sv_valund_swigconstant(_gdxcc)
sv_valund = _gdxcc.sv_valund

_gdxcc.sv_valna_swigconstant(_gdxcc)
sv_valna = _gdxcc.sv_valna

_gdxcc.sv_valpin_swigconstant(_gdxcc)
sv_valpin = _gdxcc.sv_valpin

_gdxcc.sv_valmin_swigconstant(_gdxcc)
sv_valmin = _gdxcc.sv_valmin

_gdxcc.sv_valeps_swigconstant(_gdxcc)
sv_valeps = _gdxcc.sv_valeps

_gdxcc.sv_normal_swigconstant(_gdxcc)
sv_normal = _gdxcc.sv_normal

_gdxcc.sv_acronym_swigconstant(_gdxcc)
sv_acronym = _gdxcc.sv_acronym

_gdxcc.GMS_SVIDX_UNDEF_swigconstant(_gdxcc)
GMS_SVIDX_UNDEF = _gdxcc.GMS_SVIDX_UNDEF

_gdxcc.GMS_SVIDX_NA_swigconstant(_gdxcc)
GMS_SVIDX_NA = _gdxcc.GMS_SVIDX_NA

_gdxcc.GMS_SVIDX_PINF_swigconstant(_gdxcc)
GMS_SVIDX_PINF = _gdxcc.GMS_SVIDX_PINF

_gdxcc.GMS_SVIDX_MINF_swigconstant(_gdxcc)
GMS_SVIDX_MINF = _gdxcc.GMS_SVIDX_MINF

_gdxcc.GMS_SVIDX_EPS_swigconstant(_gdxcc)
GMS_SVIDX_EPS = _gdxcc.GMS_SVIDX_EPS

_gdxcc.GMS_SVIDX_NORMAL_swigconstant(_gdxcc)
GMS_SVIDX_NORMAL = _gdxcc.GMS_SVIDX_NORMAL

_gdxcc.GMS_SVIDX_ACR_swigconstant(_gdxcc)
GMS_SVIDX_ACR = _gdxcc.GMS_SVIDX_ACR

_gdxcc.GMS_SVIDX_MAX_swigconstant(_gdxcc)
GMS_SVIDX_MAX = _gdxcc.GMS_SVIDX_MAX

_gdxcc.dt_set_swigconstant(_gdxcc)
dt_set = _gdxcc.dt_set

_gdxcc.dt_par_swigconstant(_gdxcc)
dt_par = _gdxcc.dt_par

_gdxcc.dt_var_swigconstant(_gdxcc)
dt_var = _gdxcc.dt_var

_gdxcc.dt_equ_swigconstant(_gdxcc)
dt_equ = _gdxcc.dt_equ

_gdxcc.dt_alias_swigconstant(_gdxcc)
dt_alias = _gdxcc.dt_alias

_gdxcc.GMS_DT_SET_swigconstant(_gdxcc)
GMS_DT_SET = _gdxcc.GMS_DT_SET

_gdxcc.GMS_DT_PAR_swigconstant(_gdxcc)
GMS_DT_PAR = _gdxcc.GMS_DT_PAR

_gdxcc.GMS_DT_VAR_swigconstant(_gdxcc)
GMS_DT_VAR = _gdxcc.GMS_DT_VAR

_gdxcc.GMS_DT_EQU_swigconstant(_gdxcc)
GMS_DT_EQU = _gdxcc.GMS_DT_EQU

_gdxcc.GMS_DT_ALIAS_swigconstant(_gdxcc)
GMS_DT_ALIAS = _gdxcc.GMS_DT_ALIAS

_gdxcc.GMS_DT_MAX_swigconstant(_gdxcc)
GMS_DT_MAX = _gdxcc.GMS_DT_MAX

_gdxcc.GMS_SV_UNDEF_swigconstant(_gdxcc)
GMS_SV_UNDEF = _gdxcc.GMS_SV_UNDEF

_gdxcc.GMS_SV_NA_swigconstant(_gdxcc)
GMS_SV_NA = _gdxcc.GMS_SV_NA

_gdxcc.GMS_SV_PINF_swigconstant(_gdxcc)
GMS_SV_PINF = _gdxcc.GMS_SV_PINF

_gdxcc.GMS_SV_MINF_swigconstant(_gdxcc)
GMS_SV_MINF = _gdxcc.GMS_SV_MINF

_gdxcc.GMS_SV_EPS_swigconstant(_gdxcc)
GMS_SV_EPS = _gdxcc.GMS_SV_EPS

_gdxcc.GMS_SV_ACR_swigconstant(_gdxcc)
GMS_SV_ACR = _gdxcc.GMS_SV_ACR

_gdxcc.GMS_SV_NAINT_swigconstant(_gdxcc)
GMS_SV_NAINT = _gdxcc.GMS_SV_NAINT
# This file is compatible with both classic and new-style classes.

