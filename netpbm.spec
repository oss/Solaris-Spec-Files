# This package is not relocatable.
%define nb_prefix /usr/local/netpbm

Summary: Image conversion tools
Name: netpbm
Version: 9.16
Release: 1
Group: Applications/Productivity
License: several
Source: %{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: flex

%description
Netpbm is a toolkit for manipulation of graphic images, including
conversion of images between a variety of different formats.  There
are over 220 separate tools in the package including converters for
more than 80 graphics formats.  Examples of the sort of image
manipulation we're talking about are: Shrinking an image by 10%;
Cutting the top half off of an image; Making a mirror image; Creating
a sequence of images that fade from one image to another; etc.

  (from README)

%prep
%setup -q

%build
printf "2\n%{nb_prefix}\n\n\n\n\n" | perl configure
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{nb_prefix}/bin %{buildroot}%{nb_prefix}/man/man1 \
         %{buildroot}%{nb_prefix}/man/man3 %{buildroot}%{nb_prefix}/man/man5 \
         %{buildroot}%{nb_prefix}/lib
make install INSTALLBINARIES=%{buildroot}%{nb_prefix}/bin \
	     INSTALLMANUALS1=%{buildroot}%{nb_prefix}/man/man1 \
	     INSTALLMANUALS3=%{buildroot}%{nb_prefix}/man/man3 \
	     INSTALLMANUALS5=%{buildroot}%{nb_prefix}/man/man5 \
	     INSTALLLIBS=%{buildroot}%{nb_prefix}/lib \
             INSTALLDATA=%{buildroot}%{nb_prefix}/lib

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc README* COPYRIGHT.PATENT GPL_LICENSE.txt HISTORY
%{nb_prefix}
