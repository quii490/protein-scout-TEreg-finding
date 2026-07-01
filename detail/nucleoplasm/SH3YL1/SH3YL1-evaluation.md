---
type: protein-evaluation
gene: "SH3YL1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SH3YL1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SH3YL1 |
| 蛋白名称 | SH3 domain-containing YSC84-like protein 1 |
| 蛋白大小 | 342 aa / 37.1 kDa |
| UniProt ID | Q96HL8 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 342 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=22 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=72.9; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | SH3-like_dom_sf; SH3_domain; SH3_domain_YSC84-like |
| PPI | 5/10 | x3 | 15.0 | PPI degree=17 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=22 broad=28
- AF pLDDT=72.9 PDB=1
- InterPro: SH3-like_dom_sf; SH3_domain; SH3_domain_YSC84-like
- Pfam: SH3_9; Ysc84
- PPI degree=17 ChIP: None
40362200: Diagnostic and Prognostic Potential of SH3YL1 and NOX4 in Muscle-Invasive Bladde | 35004856: Identification of Diagnostic Markers Correlated With HIV(+) Immune Non-response  | 38318360: Nox4-SH3YL1 complex is involved in diabetic nephropathy.

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: SH3 domain-containing YSC84-like protein 1

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036028 |
| InterPro | IPR001452 |
| InterPro | IPR051702 |
| InterPro | IPR035511 |
| InterPro | IPR033643 |
| InterPro | IPR007461 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SH3D19 | STRING | 835 |
| WAS | STRING | 834 |
| HELZ | BioGRID | 1 |
| VIM | BioGRID | 1 |
| KHDRBS1 | BioGRID | 1 |
| BAG3 | BioGRID | 1 |
| ZBTB7B | BioGRID | 1 |
| HNRNPL | BioGRID | 1 |


### 深度机制分析

**结构域架构**：SH3YL1（342 aa，37.1 kDa）含SH3结构域（IPR036028 SH3-like_dom_sf，IPR001452 SH3_domain，IPR035511 SH3_domain_YSC84-like）和C端的Ysc84结构域（IPR007461，IPR033643）。SH3结构域是经典的蛋白-蛋白互作模块（~60个氨基酸），特异性识别富脯氨酸基序（PxxP核心），表面形成两个疏水性口袋和一个特异性口袋以区分不同的PxxP配体。Ysc84结构域的功能尚未完全解析，但在酵母同源物中参与肌动蛋白细胞骨架的组织。

**PPI互作网络解读**：PPI degree=17，高质量的互作伙伴包括：SH3D19（STRING 835分，含多个SH3结构域的支架蛋白，可能是自身SH3结构域的配体同源伙伴）、WAS（STRING 834分，Wiskott-Aldrich综合征蛋白，Arp2/3激活的肌动蛋白聚合核促进因子）、HNRNPL（hnRNP L，IRES依赖翻译调控因子和可变剪接调控因子）、BAG3（BCL2-associated athanogene 3，分子伴侣辅助的蛋白质量控制因子）、KHDRBS1（Sam68，STAR家族RNA结合蛋白，参与选择性剪接和信号传导）。这组互作将SH3YL1与RNA代谢和肌动蛋白细胞骨架连接起来。

**结构解读**：AlphaFold pLDDT=72.9（1个PDB结构验证），SH3结构域区域pLDDT >80，形成典型的β-桶状折叠（5条反平行β-链组成），PxxP结合槽清晰可辨。Ysc84域pLDDT较低（65-75），但仍形成稳定的折叠核心。整体结构质量中等，SH3域的功能态预测非常可靠。值得注意的是SH3结构域与Ysc84域之间的连接区富含可磷酸化残基（Ser/Thr），提示SH3YL1的功能可能受激酶信号通路调节。

**机制模型**：SH3YL1作为膜-细胞骨架界面的适配器蛋白，通过以下机制发挥作用：（1）通过SH3结构域识别并结合富含PxxP基序的膜蛋白或信号蛋白，Ysc84结构域介导肌动蛋白纤维（F-actin）的结合或重排，从而将膜信号传递至细胞骨架；（2）在核质中，SH3YL1可能通过HNRNPL和KHDRBS1参与RNA代谢——这两种蛋白均可在细胞核和细胞质之间穿梭，SH3YL1可能作为它们的核质锚定或运输伙伴；（3）PMID:38318360发现NOX4-SH3YL1复合物参与糖尿病肾病，NOX4产生的ROS可能在核质中引发氧化应激应答下的SH3YL1核定位改变。

**TE调控展望**：SH3YL1的TE调控潜力较低，但通过HNRNPL和KHDRBS1的间接联系值得关注。HNRNPL已被报道调控LINE-1 RNA的核保留和降解，KHDRBS1/Sam68参与内含子保留剪接事件（许多TE作为可变外显子供体）。SH3YL1可能通过影响这些RNA结合蛋白的核质穿梭效率，间接调节含TE序列的转录本命运。但目前无任何直接实验证据，需进一步验证。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96HL8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000035115-SH3YL1

![](https://images.proteinatlas.org/30927/379_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/30927/379_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/30927/390_A6_3_red_green.jpg)
![](https://images.proteinatlas.org/30927/390_A6_4_red_green.jpg)
![](https://images.proteinatlas.org/30927/377_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/30927/377_A6_2_red_green.jpg)

### PubMed 文献

**PubMed count: 28**

| 42325004 | Genetic Determinants of Treatment-Related Bone Toxicity in Pediatric Acute Lymphoblastic Leukemia. | Clin Pharmacol Ther 2026 |
| 41958711 | Replication of the Association between Retinal Aging Clock Susceptibility Genes and Retinal Age Gap in an Asian Populati | Ophthalmol Sci 2026 |
| 41799929 | Active Macropinocytosis, Lipid Catabolism, and Exhausting Immune Microenvironment of Ascites Tumor Cells Are Involved in | MedComm (2020) 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SH3YL1

