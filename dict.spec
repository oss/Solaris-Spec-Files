Summary: Dictionary tools
Name: dict
Version: 1.0a
Release: 2
Copyright: Rutgers (?)
Group: Applications/Productivity
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: vpkg-SPROcc

%description
Dict includes dict, thes, quote, and webster, which are interactive
reference tools.

%prep
%setup -q -n dict

%build
sed "s/ncc1701/webster/" dict/Makefile > dict/Makefile1
mv dict/Makefile1 dict/Makefile
cd dict; make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin %{buildroot}/usr/local/man/man1
cd dict
install -m 0755 dict   %{buildroot}/usr/local/bin/dict
install -m 0644 dict.1 %{buildroot}/usr/local/man/man1/dict.1
for i in thes quote webster; do
   ln -s dict %{buildroot}/usr/local/bin/$i
done

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
/usr/local/bin/*
/usr/local/man/*/*
