Summary: Syntax and style checker for HTML
Name: weblint
Version: 1.020
Release: 2
License: Artistic
Group: Applications/Internet
Source: weblint-1.020.tar.gz
Requires: perl
BuildRoot: /var/tmp/%{name}-root

%description
Weblint is a syntax and minimal style checker for HTML: a perl script which
picks fluff off html pages, much in the same way traditional lint picks fluff
off C programs.  Files to be checked are passed on the command-line:

    % weblint *.html

Warnings are generated a la lint -- <filename>(line #): <warning>. E.g.:

    home.html(9): malformed heading - open tag is <H1>, but closing is </H2>

Weblint includes the following features:

    *   by default checks for HTML 3.2 (Wilbur)
    *   46 different checks and warnings
    *   Warnings can be enabled/disabled individually, as per your preference
    *   basic structure and syntax checks
    *   warnings for use of unknown elements and element attributes.
    *   context checks (where a tag must appear within a certain element).
    *   overlapped or illegally nested elements.
    *   do IMG elements have ALT text?
    *   catches elements which should only appear once
    *   flags obsolete elements.
    *   support for user and site configuration files
    *   stylistic checks
    *   checks for html which is not portable across all browsers
    *   flags markup embedded in comments, since this can confuse some browsers
    *   support for Netscape (v4), and Microsoft (v4) HTML extensions

All warnings can be enabled or disabled, using a configuration file,
$HOME/.weblintrc.  A sample configuration file, weblintrc, is included
in the distribution.  Weblint also supports a site-wide configuration
file, which lets a group of people share a common configuration.
See the man page for details.

%prep
%setup -q

%build
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/weblint
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir $RPM_BUILD_ROOT/usr/local/bin
install -m 0555 weblint $RPM_BUILD_ROOT/usr/local/bin/weblint
install -m 0644 weblintrc $RPM_BUILD_ROOT/usr/local/lib/weblint/weblintrc.rpm
install -m 0444 weblint.1 $RPM_BUILD_ROOT/usr/local/man/man1/weblint.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF

Weblint has a global configuration system; if you wish to enable the
site-wide weblintrc file, copy and edit

  /usr/local/lib/weblint/weblintrc.rpm

 and set the \$SITE_DIR variable in weblint to /usr/local/lib/weblint.

EOF

%files
%defattr(-,bin,bin)
%doc Artistic Announce ChangeLog README rc.new
/usr/local/lib/weblint
/usr/local/bin/weblint
/usr/local/man/man1/weblint.1
