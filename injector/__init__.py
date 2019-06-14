__author__ = 'Alec Thomas <alec@swapoff.org>'
__version__ = '0.17.0'
__version_tag__ = ''

import platform
from distutils.version import StrictVersion

from injector.injector import AssistedBuilder, BaseKey, BaseMappingKey, BaseSequenceKey, Binder, Binding, BindingKey, \
    BoundKey, CallError, CallableProvider, CircularDependency, ClassAssistedBuilder, ClassProvider, Error, Injector, \
    InstanceProvider, Key, ListOfProviders, MapBindProvider, MappingKey, Module, MultiBindProvider, NoScope, Provider, \
    ProviderOf, Scope, ScopeDecorator, SequenceKey, SingletonScope, ThreadLocalScope, UnknownArgument, UnknownProvider, \
    UnsatisfiedRequirement, inject, noninjectable, noscope, provider, singleton, threadlocal

__all__ = [
    ProviderOf,
    ClassAssistedBuilder,
    AssistedBuilder,
    BoundKey,
    SequenceKey,
    BaseSequenceKey,
    MappingKey,
    BaseMappingKey,
    Key,
    BaseKey,
    noninjectable,
    inject,
    provider,
    Injector,
    Module,
    threadlocal,
    ThreadLocalScope,
    singleton,
    SingletonScope,
    noscope,
    NoScope,
    ScopeDecorator,
    Scope,
    Binder,
    Binding,
    BindingKey,
    MapBindProvider,
    MultiBindProvider,
    ListOfProviders,
    InstanceProvider,
    CallableProvider,
    ClassProvider,
    Provider,
    UnknownArgument,
    UnknownProvider,
    CircularDependency,
    CallError,
    UnsatisfiedRequirement,
    Error,
]

if StrictVersion(platform.python_version()) >= StrictVersion("3.7.0"):
    from injector.aio_task_scope import AioTaskScope, aio_task

    __all__ += [AioTaskScope, aio_task]
