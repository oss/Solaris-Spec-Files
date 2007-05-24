%undefine __find_provides
%undefine __find_requires

Summary:	Smarty - the compiling PHP template engine
Name:		Smarty
Version:	2.6.18
Release:	1
License:	LGPL
Group:		Development/Other
URL:		http://smarty.php.net/
Source0:	http://smarty.php.net/distributions/Smarty-%{version}.tar.gz
Requires:	php-common
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Smarty is a template engine for PHP.  More specifically, it 
facilitates a manageable way to separate application logic and
content from its presentation.  This is best described in a
situation where the application programmer and the template 
designer play different roles, or in most cases are not the same
person.  For example, let's say you are creating a web page that
is displaying a newspaper article.  The article headline, tagline,
author and body are content elements, they contain no information
about how they will be presented.  They are passed into Smarty by
the application, then the template designer edits the templates
and uses a combination of HTML tags and template tags to format 
the presentation of these elements (HTML tables, background
colors, font sizes, style sheets, etc.) One day the programmer
needs to change the way the article content is retrieved (a change
in application logic.)  This change does not affect the template
designer, the content will still arrive in the template exactly
the same.  Likewise, if the template designer wants to completely
redesign the templates, this requires no changes to the
application logic.  Therefore, the programmer can make changes to
the application logic without the need to restructure templates,
and the template designer can make changes to templates without
breaking application logic. 

%prep
%setup -q -n Smarty-%{version}

%build

mkdir -p $RPM_BUILD_ROOT/usr/local/lib/php

%install

cp -aRf libs/* $RPM_BUILD_ROOT/usr/local/lib/php

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS COPYING.lib ChangeLog FAQ INSTALL NEWS README RELEASE_NOTES TODO
%doc demo/ misc/ unit_test/
/usr/local/lib/php/*

%changelog
* Thu May 24 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 2.6.18-1
- Update to 2.6.18-1

