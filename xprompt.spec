Summary: Ask X11 user for data in shell scripts
Name: xprompt
Version: 1.0
Release: 1
Group: User Interface/X11
Copyright: Rutgers
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
Xprompt provides a means by which programs can ask the user for one or
more responses.  I have found it especially useful for reducing the
size of my (tv)twm menus.  Instead of hardwiring alternatives into a
menu, a single script is used to call xprompt and then invoke the
appropriate thing.

  (from the README)

%prep
%setup -q -n xprompt

%build
make clean
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 xprompt %{buildroot}/usr/local/bin

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc README
/usr/local/bin/xprompt
