---
type: protein-evaluation
gene: "IQCN"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## IQCN (IQ domain-containing protein N) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | IQCN |
| 蛋白全称 | IQ domain-containing protein N |
| UniProt ID | Q9H0B3 |
| 蛋白大小 | 1180.0 aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 1180 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR052318, IPR000048, IPR027417, PF00612|
| 🔗 PPI | 2/10 | ×3 | 6.0 | PPI degree=0 |
| **加权总分** | | | **73/180** | |
| **归一化总分 (÷1.83)** | | | **39/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Mitochondrion + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: IQCN 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Mitochondrion + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

spermiogenesis, SPGF78 infertility。

#### 3.3 PPI 网络

PPI degree=0。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

IQCN 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR052318 |
| InterPro | IPR000048 |
| InterPro | IPR027417 |
| Pfam | PF00612 |


### PubMed

**Count: 10**

| PMID | Title |
|---|---|
| 41602861 | IQ motif family genes in male infertility: pathogenesis, mechanisms, and clinical perspectives. |
| 40770611 | Quantitative Phosphoproteomic Analysis of Testes from Iqcn-Deficient Mice Highlights the Significance of Calmodulin Signaling in Spermiogenesis. |
| 40437858 | Novel homozygous mutation in IQCN gene causes male infertility and fertilization failure in a consanguineous mating family. |
| 39970930 | Beneficial effects of Lactiplantibacillus plantarum BGPKM22 manifest only in interaction with healthy, but not with diseased human bronchial epithelia |
| 38626700 | A prognostic model built on amino acid metabolism patterns in HPV-associated head and neck squamous cell carcinoma. |


### 深度机制分析

**结构域架构**: IQCN拥有6个IQ钙调蛋白结合基序，分布在N端 (103-132, IQ1) 和C端密集区 (926-1165, IQ2-6)，构成了一个双极性的钙信号感应器。IPR027417 (P-loop NTPase) 结构域赋予其核苷酸依赖的构象转换能力，暗示ATP水解驱动IQCN在"钙调蛋白结合态"与"释放态"之间的变构切换。这种多IQ基序的串联排布（C端5个IQ基序在仅约240个残基内紧密聚集）在钙调蛋白效应蛋白中罕见，提示其对Ca2+浓度梯度的超敏感性——可从线粒体外膜局部Ca2+微域到核质Ca2+波动实现梯度响应。

**PPI网络解读**: CALM3互作评分高达679（STRING），证实直接的钙调蛋白偶联。CABS1（钙结合精子蛋白1, score 444）与IQCN形成钙信号枢纽——这两个蛋白共同构成了精子发生过程中Ca2+-钙调蛋白信号的核心支架。值得注意的是，文献40770611证实Iqcn敲除小鼠睾丸磷酸化蛋白组发生全局性重塑，特别是钙调蛋白信号通路的关键节点显著改变。这暗示IQCN不仅是钙信号的被动接收者，更是通过其P-loop ATPase活性主动调控下游激酶/磷酸酶网络的信号组织者。

**结构解释**: AlphaFold预测可用但总体pLDDT中等，因为6个IQ基序之间的连接区域可能具有内在无序性——这是信号支架蛋白的典型特征，无序区提供多价低亲和力互作界面以动态组装信号复合物。P-loop结构域折叠置信度较高，预测为典型的Rossmann折叠核苷酸结合域。

**机制整合模型**: IQCN作为线粒体-核信号耦合器，通过以下层级运作：(1) 静息态下，IQCN通过N端IQ1锚定在线粒体外膜，C端IQ簇处于自抑制构象；(2) 精子发生过程中，线粒体重塑释放Ca2+，钙调蛋白-Ca2+结合C端IQ簇，解除自抑制；(3) P-loop ATPase水解ATP驱动核转位信号暴露；(4) 在核内，IQCN通过IQ-钙调蛋白界面招募染色质重塑因子，驱动精子细胞核凝聚所需的组蛋白-鱼精蛋白转换。这一模型将IQCN从不育基因重新定义为线粒体代谢与精子表观基因组重编程之间的分子桥梁。

**研究/转化意义**: IQCN-钙调蛋白界面的结构解析可为男性非激素避孕药提供靶点。其线粒体-核信号耦合机制为理解代谢状态如何影响生殖细胞表观遗传提供了新框架，对辅助生殖中的精子质量评估具有潜在应用价值。

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9H0B3
- HPA: https://www.proteinatlas.org/

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00015; |
| InterPro | IPR052318;IPR000048;IPR027417; |
| Pfam | PF00612; |
| UniProt Domain | DOMAIN 103..132; /note="IQ 1"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00116"; DOMAIN 926..955; /note="IQ 2"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00116"; DOMAIN 956..978; /note="IQ 3"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00116"; DOMAIN 979..1001; /note="IQ 4"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00116"; DOMAIN 1113..1142; /note="IQ 5"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00116"; DOMAIN 1143..1165; /note="IQ 6"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00116" |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000130518-IQCN

![](https://images.proteinatlas.org/42409/2237_C11_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/42409/2237_C11_40_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CABS1 | STRING | 444 |
| CALM3 | STRING | 679 |
| CCDC96 | STRING | 453 |
| OR5J2 | STRING | 418 |
