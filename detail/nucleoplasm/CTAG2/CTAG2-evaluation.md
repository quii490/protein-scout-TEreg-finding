---
type: protein-evaluation
gene: "CTAG2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## CTAG2 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CTAG2 |
| 蛋白名称 | Cancer/testis antigen 2 |
| 蛋白大小 | 210 aa / 21.1 kDa |
| UniProt ID | O75638 |
| 评估日期 | 2026-06-27 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 210 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=25 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=46.9; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | CTAG/Pcc1 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=43 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +2 |
### 3. 分析
- HPA: Nucleoplasm; Vesicles (Approved)
- PubMed: strict=25, broad=75
- AF pLDDT: 46.9 / PDB: 0
- InterPro: CTAG/Pcc1
- Pfam: Pcc1
- PPI degree=43 / ChIP: None
38733699: Enhancing antitumor response by efficiently generating large-scale TCR-T cells t | 24457462: Expression of cancer-testis antigens MAGEA1, MAGEA3, ACRBP, PRAME, SSX2, and CTA | 35651938: Identification of Novel Characteristics in TP53-Mutant Hepatocellular Carcinoma 
### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**癌睾抗原Pcc1结构域蛋白的核质定位与免疫-TE界面**：CTAG2（Cancer/testis antigen 2, 210 aa, UniProt O75638）属于癌睾抗原（CTA）家族，拥有CTAG/Pcc1保守域（IPR015419, Pfam Pcc1 PF09341）。该家族蛋白（包括CTAG1B/NY-ESO-1, CTAG2/LAGE-1）在正常组织中仅限于睾丸生殖细胞表达，但在多种癌症（黑色素瘤、肺癌、膀胱癌、滑膜肉瘤）中被异常激活。其核质定位为Approved级别（核定位特异性9/10），伴随囊泡定位（Vesicles），提示可能存在分泌或胞外囊泡相关功能。CTAG2作为免疫治疗的肿瘤特异性靶标，其TCR-T细胞疗法的研究已取得进展（PMID:38733699）。

**CTA-TE调控的双向假说**：癌睾抗原的睾丸特异性表达模式与基因组防御的进化概念高度吻合——睾丸是piRNA通路最活跃的组织，也是TE沉默需求最高的组织。许多CTA家族成员的启动子源自TE（特别是LTR和LINE-1片段），其在癌细胞中的去抑制与全基因组DNA低甲基化导致的TE启动子去抑制共享表观遗传机制。CTAG2在核质中的功能完全未知（UniProt无功能注释），但其与MAGEA4（STRING 924）、MAGEA3（STRING 897）和MAGEA1（STRING 845）的高强度互作暗示CTA家族可能形成核内的功能模块。MAGEA家族蛋白已被报道作为泛素连接酶适配因子（MAGEA3/6-TRIM28泛素化降解AMPK, PMID:33157091），若CTAG2类似地调节核内蛋白稳定性，可能通过泛素化机制影响TE沉默因子。

**Pcc1域与相分离的潜在关联**：CTAG/Pcc1域（约130 aa）富含甘氨酸和极性氨基酸，类似于IDP的prion样结构域——Pcc1域的可能相分离行为使其可在核内形成冷凝物（如核内斑点或PML体），作为"蛋白质海绵"螯合TE转录/复制因子。CTAG2在囊泡中的定位可能反映了其参与胞外囊泡（EVs）介导的TE RNA细胞间传递——EVs中的Alu和LINE-1 RNA已在肿瘤细胞中被检测到。归一化得分68.3/100中核定位特异性36/40和新奇性45/50是候选的主要驱动力。AlphaFold pLDDT=46.9的极低置信度（暗示高度无序）进一步支持了相分离介导的功能模式。


### 补充分析 (UniProt API)

**蛋白全称**: Cancer/testis antigen 2

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR015419 |
| Pfam | PF09341 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Cancer/testis antigen 2

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR015419 |
| Pfam | PF09341 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MAGEA4 | STRING | 924 |
| MAGEA3 | STRING | 897 |
| MAGEA1 | STRING | 845 |
| MAGEA2 | STRING | 796 |
| MAGEA2B | STRING | 796 |
| MAGEA10 | STRING | 761 |
| SSX2 | STRING | 709 |
| DESI1 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O75638-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000126890-CTAG2

![](https://images.proteinatlas.org/71467/1854_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/71467/1854_C4_3_red_green.jpg)

### PubMed 文献

**PubMed count: 75**

| 42289540 | Hypoxia-driven transcriptional activation of MIR100HG by HIF-1α contributes to adaptive gene regulation in hepatocellula | Funct Integr Genomics 2026 |
| 41087166 | Placental transcriptomic profiling showed disturbance of chemokine activities and lymphocyte chemotaxis in pregnancy wit | J Matern Fetal Neonatal Med 2025 |
| 39901014 | A barley pan-transcriptome reveals layers of genotype-dependent transcriptional complexity. | Nat Genet 2025 |