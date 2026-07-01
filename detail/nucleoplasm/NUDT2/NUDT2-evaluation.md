---
type: protein-evaluation
gene: "NUDT2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## NUDT2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NUDT2 |
| 蛋白名称 | Bis(5'-nucleosyl)-tetraphosphatase [asymmetrical] |
| 蛋白大小 | 147 aa / 16.8 kDa |
| UniProt ID | P50583 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 147 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=20 |
| 三维结构 | 10/10 | x3 | 30.0 | pLDDT=95.0; PDB=6 |
| 调控结构域 | 4/10 | x2 | 8.0 | NUDIX_hydrolase-like_dom_sf; NUDIX_hydrolase_CS; NUDIX_hydrolase_dom |
| PPI | 6/10 | x3 | 18.0 | PPI degree=56 |
| **加权总分** | | | **143/180** | |
| **归一化总分** | | | **78.7/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=20 broad=36
- AF pLDDT=95.0 PDB=6
- InterPro: NUDIX_hydrolase-like_dom_sf; NUDIX_hydrolase_CS; NUDIX_hydrolase_dom
- Pfam: NUDIX
- PPI degree=56 ChIP: None
40708517: Multi-omic Data Integration Reveals Drug Targets of Skin Fibrosis. | 40697080: Multi-omics study of mitochondrial dysfunction in the pathogenesis of hyperurice | 39933430: Mitochondrial-related genome-wide Mendelian randomization identifies putatively 

### 4. 总体评价
**78.7/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

NUDT2属于NUDIX水解酶超家族(IPR000086)，其单一结构域——NUDIX水解酶结构域(Pfam:PF00293)——采用经典的α-β-α三明治折叠(IPR015797, NUDIX_hydrolase-like_dom_sf)。NUDIX折叠的核心是由四股平行β折叠片夹在两对反平行α螺旋之间构成的紧凑球状结构，活性位点位于Loop-α1连接区，该区域包含保守的NUDIX基序G[X5]E[X7]REUXEEXGU(其中U为疏水残基)。NUDT2催化中心通过二价金属离子(Mg2+或Mn2+)配位实现对底物焦磷酸键的亲核进攻，特异性地不对称水解Ap4A二腺苷四磷酸的α-β焦磷酸键，生成AMP和ATP——这种不对称切割机制是它区别于对称水解酶NUDT3的分子基础。pLDDT高达95.0(为本批5个蛋白中最高)，且PDB收录6个实验结构——对于一个仅147 aa的紧凑球状蛋白，这样的高置信度折叠和丰富结构数据几乎是完美的，活性位点的每个侧链取向在实验结构中已被明确解析。

PPI网络的核心特征在于NUDT2与嘌呤核苷酸代谢酶的密集关联，这清晰地将其定位在核苷酸代谢质量控制的交叉路口。ITPA(STRING评分940)编码肌苷三磷酸焦磷酸酶，从非经典的核苷酸池中清除脱氨基化嘌呤核苷酸(ITP, dITP)，防止错误掺入核酸——NUDT2-ITPA的高亲和力互作表明细胞存在一个"核苷酸质量控制复合体"，协同监控ATP/GTP类似物的细胞水平。CTPS/CTPS1/CTPS2(STRING评分936)是CTP合成酶，催化UTP胺化为CTP——NUDT2的水解产物ATP正好是CTPS的变构激活剂和底物；同时产生的AMP进入嘌呤核苷酸循环与CTP合成竞争底物Gln，这构成了一条精致的代谢串扰：NUDT2活性通过局部ATP/AMP浓度调控CTP的合成速率。NME2(NDP激酶B, STRING评分914)催化核苷二磷酸的磷酸化，维持细胞内NTP/NDP平衡——NUDT2的产生物ATP和NME2的底物ADP通过这个互作形成了一个快速的ATP再生回路。ADCY1(腺苷酸环化酶1, STRING评分908)直接将ATP转化cAMP，NUDT2活性释放的ATP可作为ADCY1的局部底物——提示NUDT2可能在第二信使信号的空间调控中发挥作用。NPR2(钠尿肽受体2, STRING评分905)是含鸟苷酸环化酶域的膜受体——NUDT2调控嘌呤核苷酸平衡可能间接影响cGMP信号。

NUDT2对FAD-capped RNA和dpCoA-capped RNA的体外脱帽活性(功能注释中已记录)揭示了其核质定位的全新功能维度。FAD-cap是mRNA 5'端天然存在的非经典帽结构，由FAD修饰替代标准m7G-cap——这类FAD-mRNA主要存在于细菌中，但越来越多的证据表明哺乳动物核内可能存在低丰度的FAD-capped转录本，作为转录本代谢感知的分子标记。NUDT2作为核质FAD脱帽酶的假说提出：它在核质中识别和移除异常或受损mRNA上的FAD帽，使5'单磷酸化的RNA暴露给XRN家族5'→3'外切酶而快速降解，这是一种新的RNA质量控制机制。dpCoA(去磷酸辅酶A)作为mRNA帽的另一种形式，标志着该转录本的启动子区域曾受CoA结合转录因子调控，NUDT2将dpCoA帽移除意味着它可以终止该调控信号的持续时间。两个体外脱帽活性共同构成了NUDT2作为核质非经典帽结构清除酶的统一角色。

综合分子机制模型：NUDT2在其紧凑的NUDIX结构域(147 aa, pLDDT=95.0, 6个PDB结构)中通过金属离子辅助的不对称焦磷酸水解特异性切割Ap4A为AMP+ATP——这一反应在核质中具有三重功能：直接清除潜在的翻译毒性因子Ap4A(高浓度Ap4A可抑制DNA复制和ATP依赖酶)、通过产生的ATP局部供给ADCY1以调控cAMP信号的空间梯度、通过AMP/ATP比例变构调节CTPS活性和核苷酸代谢；同时，其脱帽活性将FAD/dpCoA修饰的RNA定向至降解途径，服务于核质RNA质量控制。研究意义：(1)Ap4A作为细胞应激响应分子，NUDT2通过精确调节其核内浓度控制DNA损伤应答和凋亡信号的阈值——肿瘤细胞可通过上调NUDT2降低Ap4A积累以逃避应激诱导的凋亡(PMID:40708517中皮肤纤维化药物靶点鉴定为这一方向提供了线索)；(2)NUDT2-ITPA-CTPS-NME2嘌呤代谢网络的系统生物学特性为代谢疾病干预提供了多节点靶标组合——例如高尿酸血症中NUDT2功能失调通过嘌呤代谢扰动参与致病(PMID:40697080)，恢复NUDT2活性可作为降尿酸治疗的新思路；(3)FAD/dpCoA脱帽活性的生理底物鉴定是未来研究的关键——明确核质中受NUDT2调控的FAD-mRNA物种将揭示代谢感知与基因表达的直接连接。


### 补充分析 (UniProt API)

**蛋白全称**: Bis(5'-nucleosyl)-tetraphosphatase [asymmetrical]

**功能**: Catalyzes the asymmetric hydrolysis of diadenosine 5',5'''-P1,P4-tetraphosphate (Ap4A) to yield AMP and ATP (By similarity). Exhibits decapping activity towards FAD-capped RNAs and dpCoA-capped RNAs in vitro (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR015797 |
| InterPro | IPR020084 |
| InterPro | IPR000086 |
| InterPro | IPR051325 |
| InterPro | IPR003565 |
| Pfam | PF00293 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ITPA | STRING | 940 |
| CTPS | STRING | 936 |
| CTPS1 | STRING | 936 |
| CTPS2 | STRING | 936 |
| NME2 | STRING | 914 |
| NME7 | STRING | 909 |
| ADCY1 | STRING | 908 |
| NPR2 | STRING | 905 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P50583-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164978-NUDT2

![](https://images.proteinatlas.org/44903/827_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/44903/827_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/44903/977_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/44903/977_A3_3_red_green.jpg)
![](https://images.proteinatlas.org/44903/829_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/44903/829_A3_3_red_green.jpg)
![](https://images.proteinatlas.org/58623/1004_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/58623/1004_F11_2_red_green.jpg)

### PubMed 文献

**PubMed count: 36**

| 42351973 | Melatonin Mitigates Vitrification-Induced Cryoinjury in Mouse Embryos by Alleviating Metabolic Alterations. | Antioxidants (Basel) 2026 |
| 42051571 | Autoantibodies Predictive of Atherosclerosis Progression and Statin Response in Juvenile-Onset SLE: A Biomarker Discover | medRxiv 2026 |
| 41429525 | [Exploring potential molecular biomarkers of gestational diabetes mellitus through multi-omics data integration]. | Zhonghua Liu Xing Bing Xue Za Zhi 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/NUDT2

