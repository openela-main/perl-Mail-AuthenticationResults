Name:           perl-Mail-AuthenticationResults
Version:        2.20210112
Release:        4%{?dist}
Summary:        Object Oriented Authentication-Results Headers
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Mail-AuthenticationResults/
Source0:        http://www.cpan.org/modules/by-module/Mail/Mail-AuthenticationResults-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl >= 0:5.008
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
Object Oriented Authentication-Results email headers.


%prep
%setup -q -n Mail-AuthenticationResults-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%license LICENSE
%doc Changes dist.ini README README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 2.20210112-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.20210112-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.20210112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Xavier Bachelot <xavier@bachelot.org> 2.20210112
- Update to 2.20210112 (RHBZ#1915573)

* Tue Aug 25 2020 Xavier Bachelot <xavier@bachelot.org> 1.20200824.1
- Update to 1.20200824.1 (RHBZ#1871904)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20200331.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.20200331.1-2
- Perl 5.32 rebuild

* Mon Apr 20 2020 Xavier Bachelot <xavier@bachelot.org> 1.20200331.1
- Update to 1.20200331.1 (RHBZ#1825822)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20200108-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Xavier Bachelot <xavier@bachelot.org> 1.20200108-1
- Update to 1.20200108 (RHBZ#1789387).

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20180923-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.20180923-3
- Perl 5.30 rebuild

* Mon Apr 15 2019 Xavier Bachelot <xavier@bachelot.org> 1.20180923-2
- Review fixes.

* Thu Apr 11 2019 Xavier Bachelot <xavier@bachelot.org> 1.20180923-1
- Initial package.
