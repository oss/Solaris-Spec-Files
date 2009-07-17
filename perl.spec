#%include perl-header.spec
# Don't include the perl-header, all macros needed are below.
# Some macros defined in the header prevent easy upgrade to new version of
# perl without breaking current stable versions.
#
# Just a reminder, when OSS stablizes on a new version, be sure to update
# the perl-header file.
#

%define perl_version	  5.10.0
%define perl_release      1
%define perl_prefix	  %{_prefix}/perl5
%define perl_arch	  sun4-solaris-thread-multi
%define global_perl	  %{perl_prefix}/lib/%{perl_version}
%define global_perl_arch  %{global_perl}/%{perl_arch}
%define site_perl	  %{perl_prefix}/lib/site_perl/%{perl_version}
%define site_perl_arch	  %{site_perl}/%{perl_arch}
%define perl_binary	  %{perl_prefix}/bin/perl


Name:		perl
Version:	%{perl_version}
Release:	%{perl_release}
Group:          Development/Languages
License:	GPL/Artistic
URL:		http://www.perl.org
Source:		http://www.cpan.org/src/perl-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: 	gdbm db

Summary:        The Practical Extraction and Report Language

%description
Perl is an extremely powerful scripting language that is widely used
both as an administration tool and as one of the languages of choice
for CGI scripts.  Install this if you want to use perl.

%package devel
Group:		Development/Languages
Requires:	perl = %{version}-%{release}

Summary:        Perl header files and static libraries

%description devel
Perl-devel contains the Perl header files and static libraries.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
export PATH

sh Configure \
	-de -Dprefix=%{perl_prefix} -Dusethreads 	\
	-Dldflags='-L/usr/local/lib -R/usr/local/lib' 	\
	-Dinstallprefix="%{buildroot}%{perl_prefix}"

gmake -j3
gmake test

%install
rm -rf %{buildroot}

for d in bin usr/bin usr/local/bin ; do
    mkdir -p %{buildroot}/$d
done

gmake install

# Get rid of .packlist
find %{buildroot} -name '.packlist' -exec rm -f '{}' \;

# Remove build root from Config.pm
sed -i 's:%{buildroot}::g' %{buildroot}%{global_perl_arch}/Config.pm

cat << EOF > MAIN-LIST
%defattr(-, root, root)
%doc Copying Artistic README
EOF

cat << EOF > DEVEL-LIST
%defattr(-, root, root)
EOF

find %{buildroot}%{perl_prefix} -type d \
    | sed 's:^%{buildroot}/*:%dir /:' >> MAIN-LIST

find %{buildroot} ! -type d ! \( -name '*.h' -o -name '*.a' \) -print \
    | sed 's:^%{buildroot}/*:/:' >> MAIN-LIST

find %{buildroot} \( -name '*.h' -o -name '*.a' \) -print \
    | sed 's:^%{buildroot}/*:/:' >> DEVEL-LIST

unhardlinkify.py %{buildroot}

%clean
rm -rf %{buildroot}

%files -f MAIN-LIST

%files devel -f DEVEL-LIST

%changelog
* Fri Jul 17 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 5.10.0-1
- Updated to version 5.10.0
- Added changelog
