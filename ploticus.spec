Name: ploticus
Version: 2.11
Release: 0
Summary: Makes Prett pictures
Source: plsrc211.tar.gz
Copyright: GPL
Group: Applications/Image
BuildRoot: /var/tmp/plsrc211-root
Patch0: plmakefile.patch
%description
Ploticus is good at making the types of graphs that you would see in journals for medical and social sciences, newspapers and news magazines, business publications, and so on. Ploticus is pretty good at handling date, time, and category data. Ploticus has flexibility with regard to styles and colors. Ploticus is well-suited for automated or repetitive tasks. 

%prep
%setup -q -n plsrc211
%patch0  

%build
cd src
#%ifarch sparc64
#%ifos solaris2.9
#ln -s gd13/gd.h gd.h
#%endif
#%endif
gmake

%install
cd src
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
make install RPM_BUILD_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/*
