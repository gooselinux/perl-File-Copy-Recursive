Name: 		perl-File-Copy-Recursive
Version: 	0.38
Release: 	4%{?dist}
Summary: 	Extension for recursively copying files and directories 
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/File-Copy-Recursive/
Source0: 	http://www.cpan.org/modules/by-module/File/File-Copy-Recursive-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch: noarch

BuildRequires:	perl(Test::More)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec)

%description
This module copies and moves directories recursively to an optional depth and
attempts to preserve each file or directory's mode.

%prep
%setup -q -n File-Copy-Recursive-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/File
%{_mandir}/man3/*

%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.38-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 13 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.38-1
- Upstream update.

* Fri Oct 10 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.37-1
- Upstream update.

* Wed Apr 23 2008 Ralf Corsépius <rc040203@freenet.de> - 0.36-1
- Upstream update.

* Sat Feb  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.35-2
- rebuild for new perl

* Wed Aug 29 2007 Ralf Corsépius <rc040203@freenet.de> - 0.35-1
- Upstream update.

* Mon May 14 2007 Ralf Corsépius <rc040203@freenet.de> - 0.33-2
- BR: perl(Test::More).

* Mon May 14 2007 Ralf Corsépius <rc040203@freenet.de> - 0.33-1
- Upstream update.

* Mon Mar 12 2007 Ralf Corsépius <rc040203@freenet.de> - 0.31-2
- BR: perl(ExtUtils::MakeMaker).

* Fri Mar 02 2007 Ralf Corsépius <rc040203@freenet.de> - 0.31-1
- Upstream update.

* Thu Jan 18 2007 Ralf Corsépius <rc040203@freenet.de> - 0.30-2
- Cosmetics.

* Wed Jan 17 2007 Ralf Corsépius <rc040203@freenet.de> - 0.30-1
- Initial Fedora submission.
