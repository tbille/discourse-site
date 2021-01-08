---
layout: default
permalink: /
---

<p>Once you have deployed Kubeflow, it is time to access the Kubeflow dashboard.</p>
<h3>1. Get authentication credentials</h3>
<p>To display your access credentials, run the following commands:</p>
<pre><code class="lang-bash">juju config dex-auth static-username
juju config dex-auth static-password
</code></pre>
<p>By default, these are both empty. If you wish to set them, add the relevant string to the end of the command, e.g.</p>
<pre><code class="lang-bash">juju config dex-auth static-username admin
juju config dex-auth static-password AxWiJjk2!hu4fFga7
</code></pre>
<h3>2. Find the IP address of the Kubeflow dashboard</h3>
<p>To find the IP address of the Kubeflow dashboard for your deployment run:</p>
<pre><code>kubectl get services -n kf
</code></pre>
<p>where <code>kf</code> is the name you gave to your Juju model, and hence the namespace of your Kubeflow deployment.</p>
<h3>3. Access the dashboard</h3>
<p>For local Kubeflow deployments, such as in a workstation, you can simply access the link found in the previous step, appending <code>xip.io</code>, for example: <code>http://10.64.140.43.xip.io</code>.</p>
<p>However, for remote deployments, or running on a virtual machine, creating a SOCKS proxy is required to access the dashboard. This can be done as follows:</p>
<ol>
<li>
<p>Logout from the current session with the <code>exit</code> command</p>
</li>
<li>
<p>Re-establish connection to the machine using  <code>ssh</code> with SOCKS proxy enabled through the  <code>-D9999</code>  parameter. As in the example below:</p>
<pre><code>ssh -D9999 ubuntu@&lt;machine_public_ip&gt;
</code></pre>
</li>
<li>
<p>On your computer, go to  <code>Settings &gt; Network &gt; Network Proxy</code>, and enable SOCKS proxy pointing to:  <code>127.0.0.1:9999</code></p>
</li>
<li>
<p>On a new browser window, access the link given in the previous step, appended by <code>.xip.io</code>, for example: <code>http://10.64.140.43.xip.io</code></p>
</li>
</ol>