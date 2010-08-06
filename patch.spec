Name:      patch
Version:   2.6.1
License:   GPL
Group:     Development/Tools
Summary:   Applies diff output to an original file
Release:   1
URL:       http://ftp.gnu.org/gnu/patch/
Source:    http://ftp.gnu.org/gnu/patch/patch-%{version}.tar.xz
Patch0:    patch-strnlen.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Patch takes a the output of a diff and applies it to the original.
It is often used to update source trees.  Install this package if you
are developing or tracking the software where patch is used.

%prep
%setup -q
%patch0 -p1

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc"
CLAGS="-g -xO2"
LDFLAGS="-Bdirect -zdefs"
export PATH CC CFLAGS LDFLAGS
./configure --prefix=/usr/local/gnu
gmake 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
gmake install prefix=%{buildroot}/usr/local/gnu

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
%doc COPYING AUTHORS
/usr/local/gnu/bin/patch
/usr/local/gnu/share/man/man1/patch.1

%changelog
* Thu Aug 05 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.6.1
- Update to 2.6.1
