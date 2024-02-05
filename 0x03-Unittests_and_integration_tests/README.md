# 0x03. Unittests and Integration Tests  
<p>Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.</p>

<p>The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?</p>

<p>Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.</p>

<p>Integration tests will test interactions between every part of your code.</p>

<p>Execute your tests with</p>

<pre>
<code>$ python -m unittest path/to/test_file.py
</code></pre>

<h2>Resources</h2>

<p><strong>Read or watch:</strong></p>

<ul>
	<li><a href="https://intranet.alxswe.com/rltoken/a_AEObGK8jeqPtTPmm-gIA" target="_blank" title="unittest — Unit testing framework">unittest &mdash; Unit testing framework</a></li>
	<li><a href="https://intranet.alxswe.com/rltoken/PKetnACd7FfRiU8_kpe5EA" target="_blank" title="unittest.mock — mock object library">unittest.mock &mdash; mock object library</a></li>
	<li><a href="https://intranet.alxswe.com/rltoken/2ueVPK1kWZuz525FvZ1v2Q" target="_blank" title="How to mock a readonly property with mock?">How to mock a readonly property with mock?</a></li>
	<li><a href="https://intranet.alxswe.com/rltoken/mI7qc3Y42aZ7GTlLXDxgEg" target="_blank" title="parameterized">parameterized</a></li>
	<li><a href="https://intranet.alxswe.com/rltoken/x83Hdr54q4Vax5xQ2Z3HSA" target="_blank" title="Memoization">Memoization</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/NfT-nNKrNHGrDMY-Qm-1Dg" target="_blank" title="explain to anyone">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>

<ul>
	<li>The difference between unit and integration tests.</li>
	<li>Common testing patterns such as mocking, parametrizations and fixtures</li>
</ul>

<h2>Requirements</h2>

<ul>
	<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using&nbsp;<code>python3</code>&nbsp;(version 3.7)</li>
	<li>All your files should end with a new line</li>
	<li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/env python3</code></li>
	<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
	<li>Your code should use the&nbsp;<code>pycodestyle</code>&nbsp;style (version 2.5)</li>
	<li>All your files must be executable</li>
	<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
	<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
	<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code>&nbsp;and&nbsp;<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
	<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
	<li>All your functions and coroutines must be type-annotated.</li>
</ul>

<h2>Required Files</h2>

<h3><code>utils.py</code>&nbsp;(or&nbsp;<a href="https://intranet-projects-files.s3.amazonaws.com/webstack/utils.py" target="_blank" title="download">download</a>)</h3>

<p>Click to show/hide file contents</p>

<pre>

&nbsp;</pre>

<h3><code>client.py</code>&nbsp;(or&nbsp;<a href="https://intranet-projects-files.s3.amazonaws.com/webstack/client.py" target="_blank" title="download">download</a>)</h3>

<p>Click to show/hide file contents</p>

<pre>

&nbsp;</pre>

<h3><code>fixtures.py</code>&nbsp;(or&nbsp;<a href="https://intranet-projects-files.s3.amazonaws.com/webstack/fixtures.py" target="_blank" title="download">download</a>)</h3>

<p>Click to show/hide file contents</p>

<pre>

&nbsp;</pre>

<h2>Tasks</h2>

<h3>0. Parameterize a unit test</h3>

<p>mandatory</p>

<p>Familiarize yourself with the&nbsp;<code>utils.access_nested_map</code>&nbsp;function and understand its purpose. Play with it in the Python console to make sure you understand.</p>

<p>In this task you will write the first unit test for&nbsp;<code>utils.access_nested_map</code>.</p>

<p>Create a&nbsp;<code>TestAccessNestedMap</code>&nbsp;class that inherits from&nbsp;<code>unittest.TestCase</code>.</p>

<p>Implement the&nbsp;<code>TestAccessNestedMap.test_access_nested_map</code>&nbsp;method to test that the method returns what it is supposed to.</p>

<p>Decorate the method with&nbsp;<code>@parameterized.expand</code>&nbsp;to test the function for following inputs:</p>

<pre>
<code>nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
</code></pre>

<p>For each of these inputs, test with&nbsp;<code>assertEqual</code>&nbsp;that the function returns the expected result.</p>

<p>The body of the test method should not be longer than 2 lines.</p>

<p><strong>Repo:</strong></p>

<ul>
	<li>GitHub repository:&nbsp;<code>alx-backend-python</code></li>
	<li>Directory:&nbsp;<code>0x03-Unittests_and_integration_tests</code></li>
	<li>File:&nbsp;<code>test_utils.py</code></li>
</ul>

<p>&nbsp;Done?&nbsp;Help&nbsp;Check your code&nbsp;Get a sandbox</p>

<h3>1. Parameterize a unit test</h3>

<p>mandatory</p>

<p>Implement&nbsp;<code>TestAccessNestedMap.test_access_nested_map_exception</code>. Use the&nbsp;<code>assertRaises</code>&nbsp;context manager to test that a&nbsp;<code>KeyError</code>&nbsp;is raised for the following inputs (use&nbsp;<code>@parameterized.expand</code>):</p>

<pre>
<code>nested_map={}, path=("a",)
nested_map={"a": 1}, path=("a", "b")
</code></pre>

<p>Also make sure that the exception message is as expected.</p>

<p><strong>Repo:</strong></p>

<ul>
	<li>GitHub repository:&nbsp;<code>alx-backend-python</code></li>
	<li>Directory:&nbsp;<code>0x03-Unittests_and_integration_tests</code></li>
	<li>File:&nbsp;<code>test_utils.py</code></li>
</ul>

<p>&nbsp;Done?&nbsp;Help&nbsp;Check your code&nbsp;Get a sandbox</p>

<h3>2. Mock HTTP calls</h3>

<p>mandatory</p>

<p>Familiarize yourself with the&nbsp;<code>utils.get_json</code>&nbsp;function.</p>

<p>Define the&nbsp;<code>TestGetJson(unittest.TestCase)</code>&nbsp;class and implement the&nbsp;<code>TestGetJson.test_get_json</code>&nbsp;method to test that&nbsp;<code>utils.get_json</code>&nbsp;returns the expected result.</p>

<p>We don&rsquo;t want to make any actual external HTTP calls. Use&nbsp;<code>unittest.mock.patch</code>&nbsp;to patch&nbsp;<code>requests.get</code>. Make sure it returns a&nbsp;<code>Mock</code>&nbsp;object with a&nbsp;<code>json</code>&nbsp;method that returns&nbsp;<code>test_payload</code>&nbsp;which you parametrize alongside the&nbsp;<code>test_url</code>&nbsp;that you will pass to&nbsp;<code>get_json</code>&nbsp;with the following inputs:</p>

<pre>
<code>test_url="http://example.com", test_payload={"payload": True}
test_url="http://holberton.io", test_payload={"payload": False}
</code></pre>

<p>Test that the mocked&nbsp;<code>get</code>&nbsp;method was called exactly once (per input) with&nbsp;<code>test_url</code>&nbsp;as argument.</p>

<p>Test that the output of&nbsp;<code>get_json</code>&nbsp;is equal to&nbsp;<code>test_payload</code>.</p>

<p><strong>Repo:</strong></p>

<ul>
	<li>GitHub repository:&nbsp;<code>alx-backend-python</code></li>
	<li>Directory:&nbsp;<code>0x03-Unittests_and_integration_tests</code></li>
	<li>File:&nbsp;<code>test_utils.py</code></li>
</ul>

<p>&nbsp;Done?&nbsp;Help&nbsp;Check your code&nbsp;Get a sandbox</p>

<h3>3. Parameterize and patch</h3>

<p>mandatory</p>

<p>Read about memoization and familiarize yourself with the&nbsp;<code>utils.memoize</code>&nbsp;decorator.</p>

<p>Implement the&nbsp;<code>TestMemoize(unittest.TestCase)</code>&nbsp;class with a&nbsp;<code>test_memoize</code>&nbsp;method.</p>

<p>Inside&nbsp;<code>test_memoize</code>, define following class</p>

<pre>
<code>class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()
</code></pre>

<p>Use&nbsp;<code>unittest.mock.patch</code>&nbsp;to mock&nbsp;<code>a_method</code>. Test that when calling&nbsp;<code>a_property</code>&nbsp;twice, the correct result is returned but&nbsp;<code>a_method</code>&nbsp;is only called once using&nbsp;<code>assert_called_once</code>.</p>

<p><strong>Repo:</strong></p>

<ul>
	<li>GitHub repository:&nbsp;<code>alx-backend-python</code></li>
	<li>Directory:&nbsp;<code>0x03-Unittests_and_integration_tests</code></li>
	<li>File:&nbsp;<code>test_utils.py</code></li>
</ul>

<p>&nbsp;Done?&nbsp;Help&nbsp;Check your code&nbsp;Get a sandbox</p>

<h3>4. Parameterize and patch as decorators</h3>

<p>mandatory</p>

<p>Familiarize yourself with the&nbsp;<code>client.GithubOrgClient</code>&nbsp;class.</p>

<p>In a new&nbsp;<code>test_client.py</code>&nbsp;file, declare the&nbsp;<code>TestGithubOrgClient(unittest.TestCase)</code>&nbsp;class and implement the&nbsp;<code>test_org</code>&nbsp;method.</p>

<p>This method should test that&nbsp;<code>GithubOrgClient.org</code>&nbsp;returns the correct value.</p>

<p>Use&nbsp;<code>@patch</code>&nbsp;as a decorator to make sure&nbsp;<code>get_json</code>&nbsp;is called once with the expected argument but make sure it is not executed.</p>

<p>Use&nbsp;<code>@parameterized.expand</code>&nbsp;as a decorator to parametrize the test with a couple of&nbsp;<code>org</code>&nbsp;examples to pass to&nbsp;<code>GithubOrgClient</code>, in this order:</p>

<ul>
	<li><code>google</code></li>
	<li><code>abc</code></li>
</ul>

<p>Of course, no external HTTP calls should be made.</p>

<p><strong>Repo:</strong></p>

<ul>
	<li>GitHub repository:&nbsp;<code>alx-backend-python</code></li>
	<li>Directory:&nbsp;<code>0x03-Unittests_and_integration_tests</code></li>
	<li>File:&nbsp;<code>test_client.py</code></li>
</ul>

<p>&nbsp;Done?&nbsp;Help&nbsp;Check your code&nbsp;Get a sandbox</p>

<h3>5. Mocking a property</h3>

<p>mandatory</p>

<p><code>memoize</code>&nbsp;turns methods into properties. Read up on how to mock a property (see resource).</p>

<p>Implement the&nbsp;<code>test_public_repos_url</code>&nbsp;method to unit-test&nbsp;<code>GithubOrgClient._public_repos_url</code>.</p>

<p>Use&nbsp;<code>patch</code>&nbsp;as a context manager to patch&nbsp;<code>GithubOrgClient.org</code>&nbsp;and make it return a known payload.</p>

<p>Test that the result of&nbsp;<code>_public_repos_url</code>&nbsp;is the expected one based on the mocked payload.</p>

<p><strong>Repo:</strong></p>

<ul>
	<li>GitHub repository:&nbsp;<code>alx-backend-python</code></li>
	<li>Directory:&nbsp;<code>0x03-Unittests_and_integration_tests</code></li>
	<li>File:&nbsp;<code>test_client.py</code></li>
</ul>

<p>&nbsp;Done?&nbsp;Help&nbsp;Check your code&nbsp;Get a sandbox</p>

<h3>6. More patching</h3>

<p>mandatory</p>

<p>Implement&nbsp;<code>TestGithubOrgClient.test_public_repos</code>&nbsp;to unit-test&nbsp;<code>GithubOrgClient.public_repos</code>.</p>

<p>Use&nbsp;<code>@patch</code>&nbsp;as a decorator to mock&nbsp;<code>get_json</code>&nbsp;and make it return a payload of your choice.</p>

<p>Use&nbsp;<code>patch</code>&nbsp;as a context manager to mock&nbsp;<code>GithubOrgClient._public_repos_url</code>&nbsp;and return a value of your choice.</p>

<p>Test that the list of repos is what you expect from the chosen payload.</p>

<p>Test that the mocked property and the mocked&nbsp;<code>get_json</code>&nbsp;was called once.</p>

<p><strong>Repo:</strong></p>

<ul>
	<li>GitHub repository:&nbsp;<code>alx-backend-python</code></li>
	<li>Directory:&nbsp;<code>0x03-Unittests_and_integration_tests</code></li>
	<li>File:&nbsp;<code>test_client.py</code></li>
</ul>

<p>&nbsp;Done?&nbsp;Help&nbsp;Check your code&nbsp;Get a sandbox</p>

<h3>7. Parameterize</h3>

<p>mandatory</p>

<p>Implement&nbsp;<code>TestGithubOrgClient.test_has_license</code>&nbsp;to unit-test&nbsp;<code>GithubOrgClient.has_license</code>.</p>

<p>Parametrize the test with the following inputs</p>

<pre>
<code>repo={"license": {"key": "my_license"}}, license_key="my_license"
repo={"license": {"key": "other_license"}}, license_key="my_license"
</code></pre>

<p>You should also parameterize the expected returned value.</p>

<p><strong>Repo:</strong></p>

<ul>
	<li>GitHub repository:&nbsp;<code>alx-backend-python</code></li>
	<li>Directory:&nbsp;<code>0x03-Unittests_and_integration_tests</code></li>
	<li>File:&nbsp;<code>test_client.py</code></li>
</ul>

<p>&nbsp;Done?&nbsp;Help&nbsp;Check your code&nbsp;Get a sandbox</p>

<h3>8. Integration test: fixtures</h3>

<p>mandatory</p>

<p>We want to test the&nbsp;<code>GithubOrgClient.public_repos</code>&nbsp;method in an integration test. That means that we will only mock code that sends external requests.</p>

<p>Create the&nbsp;<code>TestIntegrationGithubOrgClient(unittest.TestCase)</code>&nbsp;class and implement the&nbsp;<code>setUpClass</code>&nbsp;and&nbsp;<code>tearDownClass</code>&nbsp;which are part of the&nbsp;<code>unittest.TestCase</code>&nbsp;API.</p>

<p>Use&nbsp;<code>@parameterized_class</code>&nbsp;to decorate the class and parameterize it with fixtures found in&nbsp;<code>fixtures.py</code>. The file contains the following fixtures:</p>

<pre>
<code>org_payload, repos_payload, expected_repos, apache2_repos
</code></pre>

<p>The&nbsp;<code>setupClass</code>&nbsp;should mock&nbsp;<code>requests.get</code>&nbsp;to return example payloads found in the fixtures.</p>

<p>Use&nbsp;<code>patch</code>&nbsp;to start a patcher named&nbsp;<code>get_patcher</code>, and use&nbsp;<code>side_effect</code>&nbsp;to make sure the mock of&nbsp;<code>requests.get(url).json()</code>&nbsp;returns the correct fixtures for the various values of&nbsp;<code>url</code>&nbsp;that you anticipate to receive.</p>

<p>Implement the&nbsp;<code>tearDownClass</code>&nbsp;class method to stop the patcher.</p>

<p><strong>Repo:</strong></p>

<ul>
	<li>GitHub repository:&nbsp;<code>alx-backend-python</code></li>
	<li>Directory:&nbsp;<code>0x03-Unittests_and_integration_tests</code></li>
	<li>File:&nbsp;<code>test_client.py</code></li>
</ul>

<p>&nbsp;Done?&nbsp;Help&nbsp;Check your code&nbsp;Get a sandbox</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>Copyright &copy; 2024 ALX, All rights reserved.</p>
