Summary:                 DevOps Swiss Army Knife
Name:                    devops-sak
Version:                 9999
Release:                 1
License:                 GPLv3
URL:                     https://github.com/sergiotocalini/devops-sak
Source0:                 https://github.com/sergiotocalini/devops-sak/archive/master.zip
Group:                   Development/Languages
BuildArch:               noarch
Requires:                python
Requires:                python-dns
Requires:                python-setuptools
Requires:                python-prettytable
Requires:                python-IPy

%description
DevOps Swiss Army Knife is a set of tools to help the DevOps, ItOps or SysAdmin to update manage the infrastructure in an easy way.

%prep
%setup -q -n devops-sak-master

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
                        %{python_sitelib}/devops_sak
			%{python_sitelib}/devops_sak-*-py2.*.egg-info
%attr(755,-,-)          /usr/bin/*

%changelog
* Sat Jul 23 2016 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 1.0.0
- Initial spec with devops_sak-1.0.0 version.
