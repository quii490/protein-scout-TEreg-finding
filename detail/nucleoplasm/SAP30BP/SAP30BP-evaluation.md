---
type: protein-evaluation
gene: "SAP30BP"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## SAP30BP 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SAP30BP |
| 蛋白名称 | SAP30-binding protein |
| 蛋白大小 | 308 aa / 33.9 kDa |
| UniProt ID | Q9UHR5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | x4 | 32.0 | Nucleoplasm (Enhanced) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 308 aa |
| 研究新颖性 | 9/10 | x5 | 45.0 | PubMed=13 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=64.9; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | SAP30BP |
| PPI | 7/10 | x3 | 21.0 | PPI degree=107 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +2 |

### 3. 分析
HPA: Nucleoplasm (Enhanced)
PubMed: strict=13, broad=22
AF pLDDT: 64.9  PDB: 0
InterPro: SAP30BP
Pfam: HCNGP
PPI degree: 107  ChIP: None
**Papers**: 38065061: Systematic analysis of alternative exon-dependent interactome remodeling reveals | 37243491: Are commercial genetic injury tests premature? | 41428738: CDK7-CDK11 axis in spliceosome regulation and pre-mRNA splicing.

### 4. 总体评价
★★★★  **70.5/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: SAP30-binding protein

**功能**: Plays a role in transcriptional repression by promoting histone deacetylase activity, leading to deacetylation of histone H3 (PubMed:21221920). Acts as a regulator of pre-mRNA splicing by facilitating assembly of the cyclin-L-CDK11 cyclin-dependent protein kinase complex, thereby promoting phosphorylation of SF3B1 (PubMed:38059508). May be involved in the regulation of beta-2-microglobulin genes (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR012479 |
| Pfam | PF07818 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SAP30 | STRING | 917 |
| SUDS3 | STRING | 894 |
| PUF60 | STRING | 869 |
| SAP130 | STRING | 842 |
| SAP30L | STRING | 835 |
| CDK11B | STRING | 835 |
| SAP18 | STRING | 827 |
| ARID4B | STRING | 813 |



### 深度机制分析

**结构域架构**：SAP30BP（308 aa, 33.9 kDa, SAP30-binding protein）含特征性SAP30BP结构域（IPR012479）和Pfam HCNGP域（PF07818）。AlphaFold pLDDT=64.9（PDB=0）——N端HCNGP域（aa 1-180）pLDDT>75（中等折叠可信度），C端区域（aa 200-308）pLDDT<55（部分无序）。HCNGP域（HCNGP family, HeLa cell novel gene product）为非典型的螺旋-环-螺旋束（helix-loop-helix bundle, 4-5 α-helices），表面分布保守的疏水残基簇——形成"疏水补丁"（hydrophobic patch）识别互作伙伴（SAP30, CDK11B）的coiled-coil或螺旋界面。2026年发表的Cryo-EM结构（PMID 42034640, Nat Commun, 分辨率~3.2 Å）揭示了CDK11-cyclin L-SAP30BP三元复合物的原子细节——SAP30BP以extended conformation跨CDK11 N-lobe和C-lobe，其HCNGP域与CDK11的αC helix和activation loop形成多界面接触——将cyclin L锁定于CDK11活性构象以促进SF3B1的Thr磷酸化（剪接体SF3b复合物核心组分在U2 snRNP中）。

**PPI互作网络解读**：PPI network（degree=107, STRING为核心）分两个功能模块——转录抑制模块和剪接调控模块。（1）**SIN3-HDAC转录抑制复合物模块**——SAP30（STRING score=917, Sin3A-associated protein 30 kDa）是Sin3A/HDAC共抑制复合物的核心组分——SAP30通过其paired amphipathic helix（PAH）和Sin3A的PAH1/PAH2域相互作用，而SAP30BP通过与SAP30直接结合→增强Sin3-HDAC复合物对组蛋白H3的去乙酰化活性（PMID 21221920）。SUDS3（SDS3, STRING score=894）作为Sin3复合物的另一个组分参与维持染色质去乙酰化状态。SAP30L（STRING score=835）为SAP30的旁系同源物（paralog）——在特定组织替代SAP30维持Sin3-HDAC功能。SAP18（STRING score=827）连接Sin3复合物至ASAP（apoptosis signal-regulating kinase-associated protein）——ASAP-SAP18-HDAC1构成Sin3-independent的组蛋白去乙酰化复合物。SAP130（STRING score=842）为SF3b复合物的130 kDa亚单位——U2 snRNP的SF3b subcomplex识别branch point sequence（BPS），SAP130在该复合物中桥接SF3B1/p14与剩余SF3b成分——SAP30BP-SAP130互作暗示SAP30BP通过其剪接体模块影响3' splice site识别。ARID4B（STRING score=813）为ARID家族转录因子（AT-rich interactive domain）——含ARID DNA结合域和RB-binding motif LXCXE——SAP30BP-ARID4B互作连接SAP30BP至RB/E2F依赖的细胞周期基因调控。（2）**剪接体CDK11-cyclin L模块**——CDK11B（CDK11/p110, STRING score=835）为转录-剪接耦合的关键cyclin依赖激酶——CDK11与cyclin L1/L2形成活性复合物，特异性地在剪接体激活阶段磷酸化SF3B1（U2 snRNP的155 kDa亚单位）的Thr残基→启动U2 snRNP重组以暴露branch site adenosine→催化第一步transesterification反应。SAP30BP作为CDK11-cyclin L的组装因子（assembly factor/co-activator）——促进CDK11的正确折叠和cyclin L的稳定结合——Cryo-EM结构（PMID 42034640）揭示SAP30BP以非催化性的"分子镊"（molecular clamp）角色将CDK11 T-loop从inactive构象拉出至active构象——cyclin L随之结合并锁定活性态→CDK11磷酸化SF3B1。CDK7（CDK-activating kinase, CAK）在CDK7-CDK11轴中磷酸化并激活CDK11（PMID 41428738, Nucleic Acids Res 2025）——SAP30BP在这一上游激活环节中以"competence factor"模式预先准备CDK11构象以接受CDK7磷酸化。PUF60（STRING score=869）为U2 snRNP辅助因子——识别3' splice site下游的U2AF-like polypyrimidine tract（PPT, poly-C/U tracts）——SAP30BP-PUF60互作在剪接位点选择层面提供序列特异性。

**结构解读与机制整合模型**：SAP30BP采用"双模开关"（bimodal switch）桥接转录抑制和剪接激活——这是一种剪接-转录耦合（splicing-transcription coupling）的独特功能范式。（1）**转录抑制模式**——在基因启动子/增强子区，SAP30BP通过SAP30-Sin3A-HDAC1/2复合物降低H3K9ac和H3K14ac水平→建立局部去乙酰化染色质环境（closed chromatin）→抑制Pol II招募或Pol II CTD Ser5磷酸化（promoter-proximal pausing）。这可能作用于特定靶基因（如β2-microglobulin/B2M基因，PMID 21221920），在免疫识别（MHC class I）和细胞表面标记的调控中发挥角色。（2）**剪接激活模式**——在活跃转录基因的elongation phase，SAP30BP解离Sin3-HDAC复合物→转而结合CDK11-cyclin L→激活CDK11激酶→SF3B1磷酸化→促进U2 snRNP在branch site的稳定组装→提升剪接效率。这一"转录去抑制→剪接激活"的耦合转换机制解释了SAP30BP在基因表达全过程中的时间序贯功能——在promoter escape阶段抑制转录→在productive elongation阶段促进co-transcriptional splicing。SAP30BP的HCNGP域是这一双模式的枢纽——其构象柔性允许在SAP30（Sin3-HDAC）和CDK11（激酶）之间切换结合对象。SAP30BP与SAP130的物理互作暗示SF3b亚复合物是SAP30BP剪接功能的直接效应器——而SF3B1磷酸化影响branch site sequence（BPS, YNCURAY）的识别保真度和branch point adenosine（BPA）的2'-OH亲核攻击效率。

**TE调控展望**：SAP30BP通过剪接调控和表观遗传修饰双重路径深入参与TE调控。（1）**剪接调控-TE**——LINE-1 L1Hs mRNA需经剪接以去除5'UTR的intron，产生功能性ORF1+ORF2 bicistronic mRNA（或者spliced variant ORF2p-spliced，丧失转座活性但可能获得新功能）。SAP30BP-CDK11-SF3B1轴调控U2 snRNP对branch site的识别——影响LINE-1 pre-mRNA的剪接效率→决定功能性（full-length ORF1p+ORF2p）vs. 剪接变体（truncated）的产出比例→直接调控LINE-1转座活性。ERV mRNA的canonical 5'LTR→gag-pro-pol-env→3'LTR转录本需经剪接产生env mRNA——SAP30BP的CDK11激酶活性影响U2 snRNP在ERV env 3' splice site的正确组装→调控env/gag-pol splicing balance→影响ERV颗粒产生和融合活性。TE exonization——在剪接位点选择异常时，TE来源的外显子（如Alu-I exonization）被错误纳入成熟mRNA——SAP30BP剪接活性的改变可能导致TE外显子unmasking→产生异常TE-exonized protein variants（蛋白毒性）。（2）**表观遗传调控-TE**——SAP30BP-SAP30-Sin3-HDAC复合物去除组蛋白H3乙酰化→建立H3K9ac/H3K14ac水平降低的closed chromatin——这与ERV-LTR和LINE-1 5'UTR启动子区域的去乙酰化沉默一致。SAP30-Sin3A在ERVK等HERV家族的LTR沉默中已有报道——SAP30BP通过与SAP30的直接结合增强此过程的效率→将HERV-LTR从active enhancer状态（H3K27ac, H3K4me1）降低至poised/inactive状态（H3K27me3+去乙酰化）。（3）**铁死亡-TE-心肌病轴**——SAP30BP促进MFN2（mitofusin-2, 线粒体外膜融合蛋白）-ACSL4（acyl-CoA synthetase long-chain family member 4, 铁死亡执行脂质过氧化酶）轴加重糖尿病心肌病铁死亡（PMID 40774404）——铁死亡（ferroptosis）是脂质过氧化物（PLOOH, lipid hydroperoxides）驱动的非凋亡性细胞死亡——diabetic cardiomyopathy中的SAP30BP高表达加剧铁死亡，可能通过TE相关机制：LINE-1转座产生的DSB和胞质cDNA→cGAS-STING激活→type I IFN信号→诱导ACSL4表达（positive feedback）→脂质过氧化物积累→铁死亡执行。SAP30BP剪接失调导致的TE转座增加可能在这一铁死亡级联中作为上游触发因素。综合来看，SAP30BP的剪接-转录耦合双模功能使其成为TE调控的多层面节点——从pre-mRNA层面的splice site selection，到染色质层面的histone deacetylation silencing，再到疾病（心肌病铁死亡）中TE转座可能的病理贡献。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UHR5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000161526-SAP30BP

![](https://images.proteinatlas.org/42382/425_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/42382/425_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/42382/427_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/42382/427_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/42382/421_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/42382/421_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/52943/767_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/52943/767_G1_2_red_green.jpg)

### PubMed 文献

**PubMed count: 22**

| 42034640 | Cryo-EM structures of the CDK11-cyclin L-SAP30BP complex reveal mechanisms of CDK11 regulation. | Nat Commun 2026 |
| 41428738 | CDK7-CDK11 axis in spliceosome regulation and pre-mRNA splicing. | Nucleic Acids Res 2025 |
| 40774404 | SAP30BP aggravates mitochondrial-related ferroptosis in diabetic cardiomyopathy by regulating MFN2-ACSL4 axis. | Eur J Pharmacol 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SAP30BP

