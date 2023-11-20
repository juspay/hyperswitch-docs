---
description: Deploy the Hyperswitch server on the cloud
---

# 🗄 Deploy app server

{% hint style="info" %}
In this chapter, you will deploy Hyperswitch server on AWS cloud. You can either try out a quick standalone deployment or a more scalable production ready setup
{% endhint %}

***

This guide is aimed at helping you deploy the Hyperswitch application on the cloud and access our APIs over the internet.

There are two methods in which you can deploy our application on the cloud. Depending on your requirement you can proceed with one of the following

<table><thead><tr><th width="198.33333333333331">Element</th><th>Production Ready Deployment</th><th>Standalone Deployment</th></tr></thead><tbody><tr><td>Best suited for</td><td>Production grade application</td><td>Quick prototyping and test environments</td></tr><tr><td>AWS Cost </td><td>As per your AWS usage</td><td>Easily fits with AWS Free Tier</td></tr><tr><td>App Server</td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span> (EKS)</td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span> (EC2)</td></tr><tr><td>RDS</td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>ElasticCache</td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td>Scalable</td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Monitoring</td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Load Balancer</td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Scheduler</td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>Proxies (In/Out)</td><td>Coming Soon!</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td>App Updates</td><td>Coming Soon!</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr></tbody></table>





<table data-card-size="large" data-view="cards" data-full-width="false"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Production Ready Deployment <code>Recommended</code></strong> </td><td><p></p><p>Use our CDK script to deploy a production-ready K8s setup inside your stack</p></td><td><ul><li>Setup a new K8s cluster for Hyperswitch using helm charts</li><li>Monitoring setup is included</li></ul></td><td><a href="../../.gitbook/assets/Group-42.jpg">Group-42.jpg</a></td><td><a href="production-ready-deployment.md">production-ready-deployment.md</a></td></tr><tr><td><p><strong>Standalone Deployment</strong> </p><p><strong><code>For prototyping</code></strong></p></td><td><p></p><p>Use the standalone deployment script to deploy Hyperswitch on AWS quickly</p></td><td><ul><li>Deploy in 3 steps in your own AWS account</li><li>Covered under AWS Free Tier</li></ul></td><td><a href="../../.gitbook/assets/1_q6F0j8HFHd8jeYXyQBqrCQ.jpg">1_q6F0j8HFHd8jeYXyQBqrCQ.jpg</a></td><td><a href="standalone-deployment-for-prototyping.md">standalone-deployment-for-prototyping.md</a></td></tr></tbody></table>

### Choose the right deployment method
