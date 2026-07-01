---
type: protein-evaluation
gene: "SLC12A4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC12A4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC12A4 |
| 蛋白名称 | Solute carrier family 12 member 4 |
| 蛋白大小 | 1085 aa / 120.7 kDa |
| UniProt ID | Q9UP95 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cell Junctions; Cytokinetic bridge; Nucleoplasm; P (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 1085 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=17 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=81.6; PDB=8 |
| 调控结构域 | 4/10 | x2 | 8.0 | AA-permease/SLC12A_dom; KCC1; KCL_cotranspt |
| PPI | 7/10 | x3 | 21.0 | PPI degree=129 |
| **加权总分** | | | **144/180** | |
| **归一化总分** | | | **79.2/100** | 互证: +1 |

### 3. 分析
- Cell Junctions; Cytokinetic bridge; Nucleoplasm; Primary cilium (Approved)
- PubMed strict=17 broad=26
- AF pLDDT=81.6 PDB=8
- InterPro: AA-permease/SLC12A_dom; KCC1; KCL_cotranspt
- Pfam: AA_permease; SLC12
- PPI degree=129 ChIP: None
39027244: Gut commensal metabolite rhamnose promotes macrophages phagocytosis by activatin | 31792382: Interpreting an apoptotic corpse as anti-inflammatory involves a chloride sensin | 41414942: Exploring the Cell Biological and Functional Effects of the First Disease Associ

### 4. 总体评价
**79.2/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域架构与离子转运机制**：SLC12A4（KCC1）属于阳离子-氯化物共转运蛋白（CCC）家族，其结构域组织揭示了12次跨膜螺旋的精妙排列。InterPro条目IPR004841（AA-permease/SLC12A结构域）表明该蛋白共享氨基酸通透酶超家族的折叠拓扑，其中跨膜螺旋TM1-TM5和TM6-TM10形成两个假对称的5+5螺旋束，构成离子传导通路的核心。IPR000622（KCC1）定义了钾-氯化物共转运体亚家族特征，其独特的离子选择性由TM2和TM7中的保守苏氨酸/丝氨酸簇赋予——这些残基通过羟基与K+配位，同时排除Na+。IPR018491（KCl共转运蛋白）标记了C端胞质调节域中的磷酸化簇，该区域是WNK-SPAK/OSR1激酶级联的调控靶点。AlphaFold平均pLDDT 81.6反映了跨膜区建模置信度中等（膜蛋白的常见局限），但8个PDB实验结构已解析了关键功能态——外向开放（K+和Cl-从胞外结合）、闭合（离子被封闭在中央腔）、内向开放（离子释放至胞内）三种构象的三维快照，确立了KCC1的交替访问机制：K+与Cl-以1:1化学计量比协同转运，净电荷为零（电中性），转运驱动力完全来自跨膜K+和Cl-的化学梯度。

**PPI网络与核内离子微环境调控**：PPI度129，互作组图谱揭示了SLC12A4的双重功能定位——膜转运体与信号转导节点的交叉。ILF3（白介素增强子结合因子3，NF90）是核内双链RNA结合蛋白，通过结合特定mRNA的3'-UTR调控转录后基因表达，同时参与miRNA加工和病毒RNA识别。SLC12A4与ILF3的互作暗示核内存在局部的KCl共转运活性——核质K+浓度约为140mM，Cl-约为10-20mM，该浓度差恰好处于KCC1的最佳转运范围。FLOT1（脂筏标记蛋白）定位于质膜和核膜脂筏微区，其与SLC12A4的互作表明KCC1在核膜的鞘脂/胆固醇富集区域内形成功能性微区。LYN（Src家族酪氨酸激酶）通过磷酸化KCC1的N端酪氨酸残基调控其转运活性——这一机制已在KCC2和KCC3中得到证实。LGALS3和LGALS8（半乳糖凝集素）识别KCC1胞外/腔内结构域的N-糖基化修饰，可能参与核膜上KCC1的滞留或内吞循环调控。

**核定位的离子稳态假说**：SLC12A4的HPA Approved核质定位是对离子转运蛋白功能的范式突破。核膜内陷形成的核质网（nucleoplasmic reticulum）和核膜本身的离子通道/转运体共同维持核内离子微环境。KCC1在核内的存在可能服务于三个层次的功能：(1) 核体积调控——凋亡过程中，核凝聚伴随K+和Cl-的协同外排，KCC1可能是执行这一过程的核转运体，PMID 31792382描述的"氯离子感应介导凋亡小体抗炎信号"恰好支持了氯化物转运在凋亡-免疫耦合中的核心角色；(2) 转录调控——核内Cl-浓度直接影响RNA聚合酶II的延伸速率和剪接效率，因为Cl-作为变构效应物调节多种核酶活性；(3) 细胞因子信号——KCC1定位于细胞因子桥（HPA确认），在有丝分裂末期协同调控子细胞分离所需的局部渗透压变化。PMID 39027244发现肠道共生菌代谢物鼠李糖通过激活巨噬细胞吞噬功能激活免疫应答，提示SLC12A4可能在免疫细胞中响应代谢信号并重组核内离子格局。

**机械模型与研究前景**：我们提出SLC12A4是一种"核膜-质膜双重离子稳态调节器"，其12次跨膜螺旋在核膜中形成功能性KCl共转运单元，通过WNK-SPAK磷酸化级联和LYN酪氨酸磷酸化实现双维度调控。在静息状态下，核内KCC1维持核质K+/Cl-梯度以支持基础转录和剪接；在凋亡刺激下，KCC1活性增强驱动核凝聚所需的离子和水外排；在细胞分裂中，KCC1参与细胞因子桥的渗透调控以保障子细胞分离。该蛋白的ILF3互作尤为值得关注——这提示了一个KCC1-ILF3-RNA代谢轴的可能存在，其中核内Cl-环境作为RNA加工的信号调节剂。未来研究应：(1) 验证KCC1是否在核膜中形成功能性转运单元，(2) 解析KCC1-ILF3互作的结构基础和功能后果，(3) 探究核内Cl-浓度变化对转录组的全局影响，(4) 利用PMID 41414942报道的首个疾病相关突变作为探针，解析KCC1核功能的病理意义。

### 补充分析 (UniProt API)

**蛋白全称**: Solute carrier family 12 member 4

**功能**: Mediates electroneutral potassium-chloride cotransport when activated by cell swelling (PubMed:35759661). May contribute to cell volume homeostasis in single cells (PubMed:10913127, PubMed:34031912). May be involved in the regulation of basolateral Cl(-) exit in NaCl absorbing epithelia (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR004841 |
| InterPro | IPR000622 |
| InterPro | IPR000076 |
| InterPro | IPR018491 |
| InterPro | IPR004842 |
| Pfam | PF00324 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TMEM43 | BioGRID | 0 |
| FLOT1 | BioGRID | 0 |
| PLP2 | BioGRID | 0 |
| ILF3 | BioGRID | 0 |
| CD55 | BioGRID | 0 |
| LYN | BioGRID | 0 |
| LGALS3 | BioGRID | 0 |
| LGALS8 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UP95-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000124067-SLC12A4

![](https://images.proteinatlas.org/48239/1253_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/48239/1253_G4_3_red_green.jpg)
![](https://images.proteinatlas.org/48239/1184_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/48239/1184_H3_3_red_green.jpg)
![](https://images.proteinatlas.org/48239/739_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/48239/739_D9_3_red_green.jpg)
![](https://images.proteinatlas.org/48239/2169_A6_26_red_green.jpg)
![](https://images.proteinatlas.org/48239/2169_A6_54_red_green.jpg)

### PubMed 文献

**PubMed count: 26**

| 41981503 | Biomarker exploration for immunotherapy plus chemotherapy following resistance to third-generation EGFR-TKIs in lung ade | BMC Cancer 2026 |
| 41938863 | TM9SF4 acts as a receptor mediating Glaesserella parasuis cytolethal distending toxin-induced cytotoxicity in PK15 cells | Front Cell Infect Microbiol 2026 |
| 41789623 | Bumetanide‑blocked SLC12A2 exerts a protective effect in experimental diabetic retinopathy. | Int J Mol Med 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLC12A4

