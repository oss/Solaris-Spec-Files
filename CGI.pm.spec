%include perl-header.spec

Summary: CGI.pm - an easy-to-use Perl5 library for writing World Wide Web CGI scripts
Name: perl-module-CGI.pm
Version: 2.98
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: CGI.pm-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl
# note: this package requires FCGI but that is only 
# for CGI-Fast... So for now we won't bother.

Provides: perl-module-CGI
Provides: perl-module-CGI-Apache
Provides: perl-module-CGI-Carp
Provides: perl-module-CGI-Cookie
Provides: perl-module-CGI-Fast
Provides: perl-module-CGI-Pretty
Provides: perl-module-CGI-Push
Provides: perl-module-CGI-Switch
Provides: perl-module-CGI-Util

%description
You'll find very verbose documentation in the file cgi_docs.html,
located in the top level directory.  

Terser documentation is found in POD (plain old documentation) form in
CGI.pm itself.  When you install CGI, the MakeMaker program will
automatically install the manual pages for you (on Unix systems, type
"man CGI").


%prep

%setup -q -n CGI.pm-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%post

# Solaris' modules
sol_module_file_apache=%{global_perl}/lib/CGI/Apache.pm
sol_module_file_carp=%{global_perl}/lib/CGI/Carp.pm
sol_module_file_cookie=%{global_perl}/lib/CGI/Cookie.pm
sol_module_file_fast=%{global_perl}/lib/CGI/Fast.pm
sol_module_file_pretty=%{global_perl}/lib/CGI/Pretty.pm
sol_module_file_push=%{global_perl}/lib/CGI/Push.pm
sol_module_file_switch=%{global_perl}/lib/CGI/Switch.pm
sol_module_file_util=%{global_perl}/lib/CGI/Util.pm

# this rpm's files
module_file_apache=%{global_perl}/CGI/Apache.pm
module_file_carp=%{global_perl}/CGI/Carp.pm
module_file_cookie=%{global_perl}/CGI/Cookie.pm
module_file_fast=%{global_perl}/CGI/Fast.pm
module_file_pretty=%{global_perl}/CGI/Pretty.pm
module_file_push=%{global_perl}/CGI/Push.pm
module_file_switch=%{global_perl}/CGI/Switch.pm
module_file_util=%{global_perl}/CGI/Util.pm

cat << EOF
***** IMPORTANT INSTRUCTION ON HOW TO USE THESE MODULES ON SOLARIS *****
Solaris 9 comes with perl and with the CGI.pm module. 
It, however, likes to put these modules under a directory different from
this RPM. We will not delete these modules for you. You should, however, 
rename them to file.pm.solaris and make a symbolic of each module in this rpm to
that old file location.

So run commands as follows:

mv ${sol_module_file_apache} ${sol_module_file_apache}.solaris
mv ${sol_module_file_carp} ${sol_module_file_carp}.solaris
mv ${sol_module_file_cookie} ${sol_module_file_cookie}.solaris
mv ${sol_module_file_fast} ${sol_module_file_fast}.solaris
mv ${sol_module_file_pretty} ${sol_module_file_pretty}.solaris
mv ${sol_module_file_push} ${sol_module_file_push}.solaris
mv ${sol_module_file_switch} ${sol_module_file_switch}.solaris
mv ${sol_module_file_util} ${sol_module_file_util}.solaris

ln -s ${module_file_apache} ${sol_module_file_apache}
ln -s ${module_file_carp} ${sol_module_file_carp}
ln -s ${module_file_cookie} ${sol_module_file_cookie}
ln -s ${module_file_fast} ${sol_module_file_fast}
ln -s ${module_file_pretty} ${sol_module_file_pretty}
ln -s ${module_file_push} ${sol_module_file_push}
ln -s ${module_file_switch} ${sol_module_file_switch}
ln -s ${module_file_util} ${sol_module_file_util}

A copy and paste should work nicely ;-)
Report bugs to oss@nbcs.rutgers.edu

EOF

%files
%defattr(-,bin,bin)
%doc README Changes cgi-lib_porting.html cgi_docs.html examples
%{global_perl}/CGI/*
%{global_perl_arch}/auto/CGI
%{perl_prefix}/man/man3/*

