Name: m4
Version: 1.4
Release: 4
Group: Development/Languages
Source: m4-%{version}.tar.gz
Copyright: GPL
Summary: The GNU version of the macro processor
BuildRoot: /var/tmp/%{name}-root
Conflicts: vpkg-SFWgm4

%description
From the documentation:

   `m4' is a macro processor, in the sense that it copies its input to
the output, expanding macros as it goes.  Macros are either builtin or
user-defined, and can take any number of arguments.  Besides just doing
macro expansion, `m4' has builtin functions for including named files,
running UNIX commands, doing integer arithmetic, manipulating text in
various ways, recursion, etc...  `m4' can be used either as a front-end
to a compiler, or as a macro processor in its own right.

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu
make

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}/usr/local/gnu

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info \
	    /usr/local/gnu/info/m4.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
	    /usr/local/gnu/info/m4.info
fi

%files
%defattr(-,root,bin)
%doc COPYING
/usr/local/gnu/info/*info*
/usr/local/gnu/bin/m4
