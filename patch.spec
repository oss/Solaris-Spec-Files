Name: patch
Version: 2.5.4
Copyright: GPL
Group: Development/Tools
Summary: Applies diff output to an original file
Release: 4
Source: patch-2.5.4.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Patch takes a the output of a diff and applies it to the original.
It is often used to update source trees.  Install this package if you
are developing or tracking the software where patch is used.

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

%files
%defattr(-,root,bin)
%doc COPYING AUTHORS
/usr/local/gnu/bin/patch
/usr/local/gnu/man/man1/patch.1
