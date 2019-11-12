AIMMS Domain for Sphinx
=========================

As first introduction to domains, please refer to [Sphinx Domain Docs](http://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html) to document your own AIMMS code.

This AIMMS Domain is build up from the [Javascript Domain](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-javascript-domain)

Basic Usage
============

```
.. aimms:parameter:: spam(eggs)

   Spam or ham the foo.
```

This describes an AIMMS parameter called spam indexed over the eggs index.

The domains also provide roles that link back to these object descriptions. For example, to link to the parameter described in the example above, you could say

```
The function :aimms:parameter:`spam` does a similar thing.
```

As you can see, both directive and role names contain the domain name and the directive name. 



The AIMMS Domain
===================

The AIMMS domain (name aimms) provides the following directives:

```
.. aimms:module:: name
```

This directive sets the module name for object declarations that follow after. The module name is used in the global module index and in cross references. This directive does not create an object heading like py:class would, for example.

By default, this directive will create a linkable entity and will cause an entry in the global module index, unless the noindex option is specified. If this option is specified, the directive will only update the current module name.

```
.. aimms:function:: name(signature)
```

Describes an AIMMS function. If you want to describe arguments as optional use square brackets as documented for Python signatures.

You can use fields to give more details about arguments and their expected types, errors which may be thrown by the function, and the value being returned:

```
.. aimms:function:: MyFunction(href, callback[, errback])

   :attribute string href: An URI to the location of the resource.
   :attribute callback: Gets called with the object.
   :attribute errback:
       Gets called in case the request fails. And a lot of other
       text so we need multiple lines.
   :throws SomeError: For whatever reason in that case.
   :returns: Something.
```

List of supported types, following the same rules as ``aimms:function::`` :


* aimms:function::
* aimms:procedure::
* aimms:externalprocedure::
* aimms:parameter::
* aimms:elementparameter::
* aimms:stringparameter::
* aimms:set::
* aimms:variable::
* aimms:constraint::
* aimms:mathematicalprogram::
* aimms:file::
* aimms:handle::


List of supported types, following the same rules as ``aimms:module::`` :

* aimms:module::
* aimms:librarymodule::


These roles are provided to refer to the described objects:

* :aimms:func:
* :aimms:procedure:
* :aimms:librarymodule:
* :aimms:externalprocedure:
* :aimms:parameter:
* :aimms:elementparameter:
* :aimms:stringparameter:
* :aimms:set:
* :aimms:variable:
* :aimms:constraint:
* :aimms:mathematicalprogram:
* :aimms:file:
* :aimms:handle:
