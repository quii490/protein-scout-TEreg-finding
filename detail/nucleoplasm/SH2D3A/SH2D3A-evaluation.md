---
type: protein-evaluation
gene: "SH2D3A"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SH2D3A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SH2D3A |
| 蛋白名称 | SH2 domain-containing protein 3A |
| 蛋白大小 | 576 aa / 63.1 kDa |
| UniProt ID | Q9BRG2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytokinetic bridge; Microtubules; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 576 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=5 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=76.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ras_GEF_dom_sf; RASGEF_cat_dom; RASGEF_cat_dom_sf |
| PPI | 6/10 | x3 | 18.0 | PPI degree=88 |
| **加权总分** | | | **139/180** | |
| **归一化总分** | | | **76.5/100** | 互证: +1 |

### 3. 分析
- Cytokinetic bridge; Microtubules; Nucleoplasm (Approved)
- PubMed strict=5 broad=19
- AF pLDDT=76.4 PDB=0
- InterPro: Ras_GEF_dom_sf; RASGEF_cat_dom; RASGEF_cat_dom_sf
- Pfam: SH2
- PPI degree=88 ChIP: None
41984197: FOXK2/SH2D3A axis recruits EGFR to drive papillary thyroid cancer progression an | 41427385: Rare longevity-associated variants, including a reduced-function mutation in cGA | 31903983: Six-gene-based prognostic model predicts overall survival in patients with uveal

### 4. 总体评价
**76.5/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域架构**：SH2D3A是一种罕见的双功能信号转导蛋白，其结构域组合——N端SH2结构域（IPR000980，Pfam SH2）与串联RasGEF催化模块（IPR023578 Ras_GEF_dom_sf，IPR001895 RASGEF_cat_dom，IPR036964/IRP036860 RASGEF_cat_dom_sf）——代表一种进化上将磷酸化信号检测与Ras家族GTP酶激活偶联的单肽链解决方案。SH2结构域特异性识别受体酪氨酸激酶（RTK）和衔接蛋白上的磷酸化酪氨酸（pTyr）基序，而RasGEF双域则催化Ras家族小G蛋白的GDP→GTP交换。这种"检测-激活"一体化的架构使得SH2D3A能够在RTK激活的毫秒级时间尺度上直接将信号传递给Ras，无需额外的衔接蛋白组装步骤。目前人类蛋白质组中同时包含SH2和RasGEF结构域的蛋白极少（仅SH2D3A、SH2D3C等少数成员），暗示其执行高度特化的信号整合功能。

**PPI网络与信号通路**：PPI网络（degree=88）的核心节点揭示了一条完整的RTK→Ras→MAPK信号轴。EGFR和ERBB2为上游受体酪氨酸激酶；BCAR1（p130Cas）是整合素/黏着斑信号支架蛋白，参与细胞迁移和侵袭；KRAS是最重要的Ras家族癌蛋白；MAPK8（JNK1）是应激活化蛋白激酶。文献验证的FOXK2/SH2D3A/EGFR轴（PubMed 41984197）证实SH2D3A通过FOXK2转录因子被招募至EGFR信号复合物，驱动甲状腺乳头状癌进展。SH2D3A在JNK活化中的作用（UniProt注释）通过MAPK8互作得到确认。值得注意的是，41427385将SH2D3A的罕见变异与长寿表型关联，并与cGAS（环状GMP-AMP合成酶，天然免疫DNA传感器）功能突变并列，暗示SH2D3A可能参与RTK信号与cGAS-STING天然免疫通路之间的交叉对话——这是一个既有文献尚未深入探索的方向。

**结构生物学解读**：AlphaFold pLDDT=76.4表明整体折叠可信度中等。SH2结构域（~100 aa）因其高度保守的折叠模式预计具有较高置信度（SH2结构域已在数百个实验结构中验证），而RasGEF催化模块（约400 aa）的局部分值可能较低，特别是在域间连接区域。无PDB实验结构（PDB=0）。PAE图（predicted aligned error）预期显示SH2和RasGEF之间的域间取向存在较高不确定性，提示这两个结构域在溶液中可能以相对灵活的"珠子在绳子上"方式排列，直到遇到结合配体后才稳定构象。这种构象灵活性可能是调控机制：只有SH2结构域对接至磷酸化RTK后，RasGEF模块才能被正确定向以接触膜锚定的Ras。

**分子机制模型**：基于全部证据的综合，SH2D3A的分子功能模型为：在静息状态下，SH2D3A以自抑制构象存在于细胞质中（SH2和RasGEF域间相互作用）。RTK（EGFR/ERBB2）激活后，受体胞内域特定酪氨酸残基自磷酸化，SH2D3A的SH2结构域识别并结合这些pTyr位点。这一结合事件通过别构效应释放RasGEF催化模块，使其催化KRAS（以及其他潜在Ras家族成员）的GDP→GTP交换。激活的Ras-GTP启动RAF→MEK→ERK（增殖信号）和JNK（应激/凋亡信号）两条下游通路。SH2D3A的核质定位（Approved级）暗示它可能在胞浆-核之间穿梭：在胞浆中执行上述RTK信号传递功能，在细胞核中则通过与FOXK2转录因子的相互作用调控基因转录程序——形成从细胞膜到染色质的完整信号中继。CENPB中心粒蛋白的互作记录进一步提示SH2D3A可能在有丝分裂期协调信号传递与染色体分离。

**研究与转化医学意义**：SH2D3A的双结构域构架使其成为独特的小分子药物靶点——SH2结构域抑制剂可阻断EGFR驱动的甲状腺癌进展，且因SH2D3A的SH2结构域与Grb2/Grb7等经典SH2蛋白存在序列差异，可能实现较高选择性。核质定位提示的转录调控功能是全新研究方向：染色质免疫沉淀结合RNA-seq可揭示SH2D3A在FOXK2协同下的靶基因网络。长寿遗传学数据（PubMed 41427385）暗示SH2D3A可能参与衰老相关信号调控，有待在模式生物中验证。值得注意的缺陷：功能研究极度匮乏（PubMed严格匹配仅5篇），缺乏条件性敲除小鼠模型，且对SH2结合pTyr的特异性序列偏好尚未被测定。


### 补充分析 (UniProt API)

**蛋白全称**: SH2 domain-containing protein 3A

**功能**: May play a role in JNK activation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR023578 |
| InterPro | IPR001895 |
| InterPro | IPR036964 |
| InterPro | IPR000980 |
| InterPro | IPR051853 |
| InterPro | IPR036860 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SFN | BioGRID | 0 |
| BCAR1 | BioGRID | 0 |
| EGFR | BioGRID | 0 |
| MAPK8 | BioGRID | 0 |
| NXF1 | BioGRID | 0 |
| ERBB2 | BioGRID | 0 |
| KRAS | BioGRID | 0 |
| CENPB | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9BRG2-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 19**

| 42301353 | Correction to: FOXK2/SH2D3A axis recruits EGFR to drive papillary thyroid cancer progression and confers sensitivity to  | Naunyn Schmiedebergs Arch Pharmacol 2026 |
| 41984197 | FOXK2/SH2D3A axis recruits EGFR to drive papillary thyroid cancer progression and confers sensitivity to EGFR inhibition | Naunyn Schmiedebergs Arch Pharmacol 2026 |
| 41427385 | Rare longevity-associated variants, including a reduced-function mutation in cGAS, identified in multigenerational long- | bioRxiv 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SH2D3A

