Summary:       Midnight Commander visual shell
Name:          mc
Version:       4.6.1
Release:       1
Group:         System Environment/Shells
License:       GPL
URL:           http://ftp.gnu.org/gnu/mc/
Source:        http://ftp.gnu.org/gnu/mc/mc-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Midnight Commander is a visual shell much like a file manager, only with way
more features.  It is text mode, but also includes mouse support if you are
running GPM.  Its coolest feature is the ability to ftp, view tar, zip
files, and poke into RPMs for specific files.  :-)

%prep
%setup -q

%build
%configure  --enable-charset \
            --with-samba \
            --without-x \
            --with-gpm-mouse \
            --enable-vfs-mcfs
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/usr/local/share/locale/locale.alias
rm $RPM_BUILD_ROOT/usr/local/lib/charset.alias

%find_lang mc

%clean
rm -rf $RPM_BUILD_ROOT

%files -f mc.lang
%defattr(-,root,root,-)
%doc FAQ COPYING NEWS README
%{_bindir}/mc*
%{_mandir}/man1/*
%{_mandir}/*/man1/*
%{_datadir}/mc


%changelog
* Thu Aug 05 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 4.6.1
- Update to 4.6.1
