Summary: CPU-resource measuring tool
Name: time
Version: 1.7
Release: 2
Group: Development/Tools
Copyright: GPL
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
`time' is a program that measures many of the CPU resources, such as
time and memory, that other programs use.  The GNU version can format
the output in arbitrary ways by using a printf-style format string to
include various resource measurements.  Some systems do not provide
much information about program resource use; `time' reports
unavailable information as zero values.
  (from README)

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu
make CPPFLAGS="-DHAVE_WAIT3"

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
%doc COPYING NEWS README AUTHORS 
/usr/local/gnu/bin/time
/usr/local/gnu/info/time.info
