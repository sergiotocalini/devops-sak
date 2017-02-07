Summary:                 DevOps Tools.
Name:                    devops-tools
Version:                 1.0.0
Release:                 1%{?dist}
License:                 GPLv3
URL:                     https://github.com/sergiotocalini/devops-tools
Source0:                 https://github.com/sergiotocalini/devops-tools/archive/master.zip
Group:                   Development/Languages
BuildArch:               noarch
Requires:                python
Requires:                python-dns
Requires:                python-setuptools

%description
DevOps Tools is a set of tools to help the DevOps, ItOps or SysAdmin to update manage the infrastructure in an easy way.

%clean

%prep
%setup -q -n devops_tools-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
                        %{python_sitelib}/devops_tools
			%{python_sitelib}/devops_tools-*-py2.*.egg-info

%changelog
* Sat Jul 23 2016 Sergio Tocalini Joerg <sergiotocalini@gmail.com> - 1.0.0
- Initial spec with devops_tools-1.0.0 version.
