%include machine-header.spec

%define prefix /usr/local/gcc-3.0.4
%define stdc_version 3.0.4
%define gcc_version 3.0.4

Name: gcc3
Version: %{gcc_version}
Release: 1
Copyright: GPL
Group: Development/Languages
Summary: The GNU C compiler
BuildRoot: %{_tmppath}/%{name}-root
Source: gcc-%{gcc_version}.tar.gz
Provides: libstdc++.so.%{stdc_version} libstdc++.so
BuildRequires: texinfo fileutils make
%if %{max_bits} == 64
BuildRequires: vpkg-SUNWarcx
%endif
Conflicts: vpkg-SFWgcc

%description
This package contains the entire gcc distribution -- it includes gcc,
g++, g77, gcj, cpp, and libstdc++.

%package cpp
Version: %{gcc_version}
Release: 1
Copyright: GPL
Group: Development/Languages
Summary: The GNU C preprocessor
BuildRoot: /var/tmp/%{name}-root

%description cpp
This package only contains cpp.  You don't need to install this if you
install gcc.

%package -n libstdc++-v3
Version: %{stdc_version}
Release: 1
Copyright: GPL
Group: Development/Languages
Summary: GNU libstdc++
Provides: libstdc++.so.%{stdc_version} libstdc++.so

%description -n libstdc++-v3
This package contains just the libstdc++ libraries.  You don't need to
install this if you install gcc.

%prep
%setup -q -n gcc-%{gcc_version}

%define build_subdir  obj-sparc-solaris

%build
PATH="/usr/local/bin:/usr/ccs/bin:/usr/bin:/usr/local/gnu/bin:/opt/SUNWspro/bin:/usr/ucb:/usr/openwin/bin:/usr/sbin"
export PATH
rm -rf %{build_subdir}
mkdir -p %{build_subdir}
cd %{build_subdir}
%if %{max_bits} == 64
../configure --prefix=%{prefix} --enable-shared --enable-threads \
  sparcv9-sun-%{sol_os}
%else
../configure --prefix=%{prefix} --enable-shared --enable-threads
%endif
gmake

%install
PATH="/usr/local/bin:/usr/ccs/bin:/usr/bin:/usr/local/gnu/bin:/opt/SUNWspro/bin:/usr/ucb:/usr/openwin/bin:/usr/sbin"
export PATH
cd %{build_subdir}
umask 022
rm -rf %{buildroot}
mkdir -p %{buildroot}%{prefix} %{buildroot}/usr/lib
gmake install prefix=%{buildroot}%{prefix}
cp %{buildroot}%{prefix}/lib/libstdc++.so.%{stdc_version} \
   %{buildroot}/usr/lib/libstd++.so.%{stdc_version}
rm -f %{buildroot}%{prefix}/info/dir

%post
if [ -x /usr/local/bin/install-info ] ; then
    for i in gcc cpp g77 gcj cppinternals ; do
        /usr/local/bin/install-info --info-dir=%{prefix}/info \
 	     %{prefix}/info/$i.info
    done
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
    for i in gcc cpp g77 gcj cppinternals ; do
        /usr/local/bin/install-info --delete --info-dir=%{prefix}/info \
	    %{prefix}/info/$i.info
    done
fi

%post cpp
if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir=%{prefix}/info \
       %{prefix}/info/cpp.info
fi

%preun cpp
if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --delete --info-dir=%{prefix}/info \
       %{prefix}/info/cpp.info
fi

%clean
rm -rf %{buildroot}

%files 
%defattr(-, root, bin)
%doc COPYING
%{prefix}
/usr/lib/*

%files -n libstdc++-v3
%defattr(-, root, bin)
/usr/lib/*.so*
%{prefix}/lib/libstdc++.so*
%if %{max_bits} == 64
%{prefix}/lib/sparcv7/libstdc++.so*
%endif

%files cpp
%defattr(-, root, bin)
%{prefix}/bin/cpp
%{prefix}/info/cpp*
%if %{max_bits} == 64
%{prefix}/lib/gcc-lib/sparcv9-sun-%{sol_os}/%{gcc_version}/*cpp0
%else
%{prefix}/lib/gcc-lib/sparc-sun-%{sol_os}/%{gcc_version}/*cpp0
%endif
%{prefix}/man/man1/cpp.1
