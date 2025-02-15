# coding: utf-8

"""
    flyteidl/service/admin.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flyteadmin.models.core_retry_strategy import CoreRetryStrategy  # noqa: F401,E501
from flyteadmin.models.core_runtime_metadata import CoreRuntimeMetadata  # noqa: F401,E501


class CoreTaskMetadata(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'discoverable': 'bool',
        'runtime': 'CoreRuntimeMetadata',
        'timeout': 'str',
        'retries': 'CoreRetryStrategy',
        'discovery_version': 'str',
        'deprecated_error_message': 'str',
        'interruptible': 'bool',
        'cache_serializable': 'bool',
        'generates_deck': 'bool',
        'tags': 'dict(str, str)',
        'pod_template_name': 'str',
        'cache_ignore_input_vars': 'list[str]'
    }

    attribute_map = {
        'discoverable': 'discoverable',
        'runtime': 'runtime',
        'timeout': 'timeout',
        'retries': 'retries',
        'discovery_version': 'discovery_version',
        'deprecated_error_message': 'deprecated_error_message',
        'interruptible': 'interruptible',
        'cache_serializable': 'cache_serializable',
        'generates_deck': 'generates_deck',
        'tags': 'tags',
        'pod_template_name': 'pod_template_name',
        'cache_ignore_input_vars': 'cache_ignore_input_vars'
    }

    def __init__(self, discoverable=None, runtime=None, timeout=None, retries=None, discovery_version=None, deprecated_error_message=None, interruptible=None, cache_serializable=None, generates_deck=None, tags=None, pod_template_name=None, cache_ignore_input_vars=None):  # noqa: E501
        """CoreTaskMetadata - a model defined in Swagger"""  # noqa: E501

        self._discoverable = None
        self._runtime = None
        self._timeout = None
        self._retries = None
        self._discovery_version = None
        self._deprecated_error_message = None
        self._interruptible = None
        self._cache_serializable = None
        self._generates_deck = None
        self._tags = None
        self._pod_template_name = None
        self._cache_ignore_input_vars = None
        self.discriminator = None

        if discoverable is not None:
            self.discoverable = discoverable
        if runtime is not None:
            self.runtime = runtime
        if timeout is not None:
            self.timeout = timeout
        if retries is not None:
            self.retries = retries
        if discovery_version is not None:
            self.discovery_version = discovery_version
        if deprecated_error_message is not None:
            self.deprecated_error_message = deprecated_error_message
        if interruptible is not None:
            self.interruptible = interruptible
        if cache_serializable is not None:
            self.cache_serializable = cache_serializable
        if generates_deck is not None:
            self.generates_deck = generates_deck
        if tags is not None:
            self.tags = tags
        if pod_template_name is not None:
            self.pod_template_name = pod_template_name
        if cache_ignore_input_vars is not None:
            self.cache_ignore_input_vars = cache_ignore_input_vars

    @property
    def discoverable(self):
        """Gets the discoverable of this CoreTaskMetadata.  # noqa: E501

        Indicates whether the system should attempt to lookup this task's output to avoid duplication of work.  # noqa: E501

        :return: The discoverable of this CoreTaskMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._discoverable

    @discoverable.setter
    def discoverable(self, discoverable):
        """Sets the discoverable of this CoreTaskMetadata.

        Indicates whether the system should attempt to lookup this task's output to avoid duplication of work.  # noqa: E501

        :param discoverable: The discoverable of this CoreTaskMetadata.  # noqa: E501
        :type: bool
        """

        self._discoverable = discoverable

    @property
    def runtime(self):
        """Gets the runtime of this CoreTaskMetadata.  # noqa: E501

        Runtime information about the task.  # noqa: E501

        :return: The runtime of this CoreTaskMetadata.  # noqa: E501
        :rtype: CoreRuntimeMetadata
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this CoreTaskMetadata.

        Runtime information about the task.  # noqa: E501

        :param runtime: The runtime of this CoreTaskMetadata.  # noqa: E501
        :type: CoreRuntimeMetadata
        """

        self._runtime = runtime

    @property
    def timeout(self):
        """Gets the timeout of this CoreTaskMetadata.  # noqa: E501

        The overall timeout of a task including user-triggered retries.  # noqa: E501

        :return: The timeout of this CoreTaskMetadata.  # noqa: E501
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this CoreTaskMetadata.

        The overall timeout of a task including user-triggered retries.  # noqa: E501

        :param timeout: The timeout of this CoreTaskMetadata.  # noqa: E501
        :type: str
        """

        self._timeout = timeout

    @property
    def retries(self):
        """Gets the retries of this CoreTaskMetadata.  # noqa: E501

        Number of retries per task.  # noqa: E501

        :return: The retries of this CoreTaskMetadata.  # noqa: E501
        :rtype: CoreRetryStrategy
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this CoreTaskMetadata.

        Number of retries per task.  # noqa: E501

        :param retries: The retries of this CoreTaskMetadata.  # noqa: E501
        :type: CoreRetryStrategy
        """

        self._retries = retries

    @property
    def discovery_version(self):
        """Gets the discovery_version of this CoreTaskMetadata.  # noqa: E501

        Indicates a logical version to apply to this task for the purpose of discovery.  # noqa: E501

        :return: The discovery_version of this CoreTaskMetadata.  # noqa: E501
        :rtype: str
        """
        return self._discovery_version

    @discovery_version.setter
    def discovery_version(self, discovery_version):
        """Sets the discovery_version of this CoreTaskMetadata.

        Indicates a logical version to apply to this task for the purpose of discovery.  # noqa: E501

        :param discovery_version: The discovery_version of this CoreTaskMetadata.  # noqa: E501
        :type: str
        """

        self._discovery_version = discovery_version

    @property
    def deprecated_error_message(self):
        """Gets the deprecated_error_message of this CoreTaskMetadata.  # noqa: E501

        If set, this indicates that this task is deprecated.  This will enable owners of tasks to notify consumers of the ending of support for a given task.  # noqa: E501

        :return: The deprecated_error_message of this CoreTaskMetadata.  # noqa: E501
        :rtype: str
        """
        return self._deprecated_error_message

    @deprecated_error_message.setter
    def deprecated_error_message(self, deprecated_error_message):
        """Sets the deprecated_error_message of this CoreTaskMetadata.

        If set, this indicates that this task is deprecated.  This will enable owners of tasks to notify consumers of the ending of support for a given task.  # noqa: E501

        :param deprecated_error_message: The deprecated_error_message of this CoreTaskMetadata.  # noqa: E501
        :type: str
        """

        self._deprecated_error_message = deprecated_error_message

    @property
    def interruptible(self):
        """Gets the interruptible of this CoreTaskMetadata.  # noqa: E501


        :return: The interruptible of this CoreTaskMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._interruptible

    @interruptible.setter
    def interruptible(self, interruptible):
        """Sets the interruptible of this CoreTaskMetadata.


        :param interruptible: The interruptible of this CoreTaskMetadata.  # noqa: E501
        :type: bool
        """

        self._interruptible = interruptible

    @property
    def cache_serializable(self):
        """Gets the cache_serializable of this CoreTaskMetadata.  # noqa: E501


        :return: The cache_serializable of this CoreTaskMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._cache_serializable

    @cache_serializable.setter
    def cache_serializable(self, cache_serializable):
        """Sets the cache_serializable of this CoreTaskMetadata.


        :param cache_serializable: The cache_serializable of this CoreTaskMetadata.  # noqa: E501
        :type: bool
        """

        self._cache_serializable = cache_serializable

    @property
    def generates_deck(self):
        """Gets the generates_deck of this CoreTaskMetadata.  # noqa: E501

        Indicates whether the task will generate a Deck URI when it finishes executing.  # noqa: E501

        :return: The generates_deck of this CoreTaskMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._generates_deck

    @generates_deck.setter
    def generates_deck(self, generates_deck):
        """Sets the generates_deck of this CoreTaskMetadata.

        Indicates whether the task will generate a Deck URI when it finishes executing.  # noqa: E501

        :param generates_deck: The generates_deck of this CoreTaskMetadata.  # noqa: E501
        :type: bool
        """

        self._generates_deck = generates_deck

    @property
    def tags(self):
        """Gets the tags of this CoreTaskMetadata.  # noqa: E501


        :return: The tags of this CoreTaskMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CoreTaskMetadata.


        :param tags: The tags of this CoreTaskMetadata.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def pod_template_name(self):
        """Gets the pod_template_name of this CoreTaskMetadata.  # noqa: E501

        pod_template_name is the unique name of a PodTemplate k8s resource to be used as the base configuration if this task creates a k8s Pod. If this value is set, the specified PodTemplate will be used instead of, but applied identically as, the default PodTemplate configured in FlytePropeller.  # noqa: E501

        :return: The pod_template_name of this CoreTaskMetadata.  # noqa: E501
        :rtype: str
        """
        return self._pod_template_name

    @pod_template_name.setter
    def pod_template_name(self, pod_template_name):
        """Sets the pod_template_name of this CoreTaskMetadata.

        pod_template_name is the unique name of a PodTemplate k8s resource to be used as the base configuration if this task creates a k8s Pod. If this value is set, the specified PodTemplate will be used instead of, but applied identically as, the default PodTemplate configured in FlytePropeller.  # noqa: E501

        :param pod_template_name: The pod_template_name of this CoreTaskMetadata.  # noqa: E501
        :type: str
        """

        self._pod_template_name = pod_template_name

    @property
    def cache_ignore_input_vars(self):
        """Gets the cache_ignore_input_vars of this CoreTaskMetadata.  # noqa: E501

        cache_ignore_input_vars is the input variables that should not be included when calculating hash for cache.  # noqa: E501

        :return: The cache_ignore_input_vars of this CoreTaskMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._cache_ignore_input_vars

    @cache_ignore_input_vars.setter
    def cache_ignore_input_vars(self, cache_ignore_input_vars):
        """Sets the cache_ignore_input_vars of this CoreTaskMetadata.

        cache_ignore_input_vars is the input variables that should not be included when calculating hash for cache.  # noqa: E501

        :param cache_ignore_input_vars: The cache_ignore_input_vars of this CoreTaskMetadata.  # noqa: E501
        :type: list[str]
        """

        self._cache_ignore_input_vars = cache_ignore_input_vars

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CoreTaskMetadata, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CoreTaskMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
