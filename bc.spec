Name: bc
Version: 1.06
Copyright: GPL
Group: Applications/Productivity
Summary: Infix and RPN calculators at your disposal
Release: 3
Source: bc-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
GNU bc includes bc and dc, infix and RPN calculators, respectively.  bc
has a C-like syntax and can be used for quite complex calculations.

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
rm -rf %{buildroot}

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info \
		 /usr/local/gnu/info/dc.info \
		--entry="* dc: (dc).              GNU dc"
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		 /usr/local/gnu/info/dc.info
fi

%files
%defattr(-,root,bin)
%doc COPYING
/usr/local/gnu/bin/bc
/usr/local/gnu/bin/dc
/usr/local/gnu/info/dc.info
/usr/local/gnu/man/man1/bc.1
/usr/local/gnu/man/man1/dc.1
