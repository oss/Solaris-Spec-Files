# This package is not relocatable.
%define nb_prefix /usr/local/netpbm
Summary: Image conversion tools
Name: netpbm
Version: 10.18.1 
Release: 1
Group: Applications/Productivity
License: several
Source0: %{name}-%{version}.tgz
Source1: NetPBM-Makefile.config.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: flex
Requires: libpng3

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
%setup -a 0
%setup -a 1


%build
mv netpbm-10.18.1/NetPBM-Makefile.config Makefile.config
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make package pkgdir=%{buildroot}/usr/local/netpbm


%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
/usr/local/netpbm/*
