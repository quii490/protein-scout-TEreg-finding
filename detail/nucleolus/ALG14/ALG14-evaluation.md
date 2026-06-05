---
type: protein-evaluation
gene: "ALG14"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ALG14 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ALG14 |
| 蛋白大小 | 216 aa / 24.2 kDa |
| UniProt ID | Q96F25 |
| 蛋白全名 | UDP-N-acetylglucosamine transferase subunit ALG14 |
| 子定位分类 | nucleolus |
| HPA IF 主定位 | Nucleoli |
| HPA IF 附加定位 | Nucleoplasm |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24 | HPA主定位Nucleoli + Nucleoplasm；UniProt注释ER膜；定位矛盾但有核仁信号 |
| 蛋白大小 | 5/10 | ×1 | 5 | 216aa/24.2kDa，极小膜结合亚基 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 (21-40→8) |
| 三维结构 | 8/10 | ×3 | 24 | pLDDT=90.9, pct>90=73.6%；无PDB |
| 调控结构域 | 4/10 | ×2 | 8 | IPR013969 (Alg14)，ER膜适配器，无调控域 |
| PPI网络 | 6/10 | ×3 | 18 | ALG13(0.999实验), DPAGT1(0.999); N-糖基化通路 |
| **加权总分** | | | **119/180** | |
| **归一化总分 (÷1.8)** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoli (main), Nucleoplasm (additional) | Approved |
| UniProt | Endoplasmic reticulum membrane (IDA) | |
| GO-CC | GO:0005789 (ER membrane, TAS), GO:0098554 (cytoplasmic side of ER membrane, IGI), GO:0043541 (UDP-N-acetylglucosamine transferase complex, IDA) | |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

#### 3.2 蛋白大小评估

216 aa / 24.2 kDa。蛋白极小，作为 ER 膜蛋白的胞质侧适配亚基，尺寸在预期范围内。但作为独立研究目标过小。**评分: 5/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 21 |
| PubMed symbol_only | 36 |
| 主要方向 | N-糖基化、先天性肌无力综合征、多囊肾病遗传学 |

**评价**: PubMed 21 篇 (strict)，较为新颖。ALG14 主要在先天性糖基化疾病和 N-糖基化途径生化机制中研究。**评分: 8/10** (21-40篇)。

**关键文献**:
1. Averbeck N et al. (2007). "Membrane topology of the Alg14 endoplasmic reticulum UDP-GlcNAc transferase subunit." *J Biol Chem*. PMID: 17686769
2. Lu J et al. (2012). "Alg14 organizes the formation of a multiglycosyltransferase complex involved in initiation of lipid-linked oligosaccharide biosynthesis." *Glycobiology*. PMID: 22061998
3. Gang Q et al. (2022). "Genetic defects are common in myopathies with tubular aggregates." *Ann Clin Transl Neurol*. PMID: 34908252
4. Adam MP et al. (1993/updated). "Congenital Myasthenic Syndromes Overview." *GeneReviews*. PMID: 20301347
5. Zang Y et al. (2025). "Prognostic and therapeutic implications of disulfidptosis-related genes in multiple myeloma." *Front Immunol*. PMID: 41403951

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 90.9 |
| pLDDT > 90 (Very High) | 73.6% |
| pLDDT 70-90 (High) | 24.1% |
| pLDDT 50-70 (Medium) | 2.3% |
| pLDDT < 50 (Low) | 0.0% |
| 有序区域 (pLDDT>70) | 97.7% |
| 实验结构 (PDB) | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR013969 (Oligosaccharide biosynthesis protein Alg14) |
| Pfam | PF08660 (Alg14) |

ALG14 为单结构域 ER 膜适配蛋白，作为 ALG13 的膜锚定亚基参与 N-糖基化途径第二步。功能为在 ER 胞质面将 ALG13 招募至膜，催化 GlcNAc 转移。无已知的转录调控或染色质相互作用功能。**评分: 4/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (top 10):

| Partner | Score | 实验证据 | 功能 |
|---------|-------|---------|------|
| ALG13 | 0.999 | 0.471 | 催化亚基，实验互作 |
| DPAGT1 | 0.999 | 0.154 | N-糖基化第一步 |
| ALG1 | 0.979 | 0 | N-糖基化第三步 |
| ALG11 | 0.772 | 0 | N-糖基化 |
| ALG3 | 0.745 | 0 | N-糖基化 |
| ALG6 | 0.745 | 0.086 | N-糖基化 |
| ALG8 | 0.726 | 0.071 | N-糖基化，实验互作 |
| GFPT1 | 0.706 | 0 | 己糖胺途径 |
| GMPPB | 0.704 | 0 | GDP-甘露糖 |
| DPM1 | 0.703 | 0.165 | Dol-P-Man合成 |

PPI 网络完全集中于 N-糖基化途径，ALG13 和 ALG8 有实验互作证据。IntAct 互作主要为酵母 TAP 和人类 co-IP (HAUS7, TSPAN1 等膜蛋白)。通路专一性强但无核调控关联。**评分: 6/10**。

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5) — 66.1/100

**核心优势**:
1. HPA Approved Nucleoli 主定位
2. AlphaFold 极高质量预测 (97.7% 有序)
3. 中度新颖 (21 篇)
4. N-糖基化途径功能明确

**风险/不确定性**:
1. HPA 核仁定位与 UniProt ER 膜矛盾，需独立验证
2. 蛋白极小
3. 功能为 ER 代谢酶适配器，与核功能关联弱
4. PPI 网络局限于 N-糖基化途径

**下一步建议**:
- [ ] 独立实验验证 ALG14 的核仁定位
- [ ] 解析 HPA 核仁信号与 ER 标记的共定位
- [ ] 评估核仁 ALG14 是否具有非经典功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96F25
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96F25
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ALG14%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000172339-ALG14
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000172339-ALG14/subcellular

![](https://images.proteinatlas.org/31829/372_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/31829/372_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/31829/374_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/31829/374_F5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96F25-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
