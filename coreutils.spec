Summary: The GNU Core Utilities are the basic file, shell and text manipulation utilities of the GNU operating system.
Name: coreutils
Version: 5.0
Release: 4
Group: General/Tools
Copyright: GPL
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Obsoletes: textutils fileutils sh-utils
Provides: textutils fileutils sh-utils

%description
The GNU Core Utilities are the basic file, shell and text manipulation utilities of the GNU operating system. These are the core utilities which are expected to exist on every operating system.

Previously these utilities were offered as three individual sets of GNU utilities, fileutils, shellutils, and textutils. Those three have been combined into a single set of utilities called the coreutils.

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu
make 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
make install prefix=%{buildroot}/usr/local/gnu

%clean
rm -fr %{buildroot}

%post
if [ -x /usr/local/bin/install-info ]; then
    /usr/local/bin/install-info --info-dir=/usr/local/gnu/info \
        --entry="* Time: (time).        GNU time" \
        /usr/local/gnu/info/time.info
fi

%preun
if [ -x /usr/local/bin/install-info ]; then
    /usr/local/bin/install-info --info-dir=/usr/local/gnu/info --delete \
        /usr/local/gnu/info/time.info
fi

%files
%defattr(-,root,bin)
/usr/local/gnu/*
