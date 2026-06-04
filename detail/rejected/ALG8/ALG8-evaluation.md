---
type: protein-evaluation
gene: "ALG8"
date: 2026-06-03
tags: [protein-scout, rejected]
status: rejected
rejection_reason: nuclear_score ≤ 3
---

## ALG8 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ALG8 |
| 蛋白大小 | 526 aa / 60.1 kDa |
| UniProt ID | Q9BVK2 |
| 蛋白全名 | Dolichyl pyrophosphate Glc1Man9GlcNAc2 alpha-1,3-glucosyltransferase |
| HPA IF 主定位 | Nucleoplasm |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-03 |
| 评估结果 | **REJECTED** (nuclear_score=3) |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA主定位Nucleoplasm；UniProt注释ER膜(lumenal side)；定位矛盾显著 |
| 蛋白大小 | 9/10 | ×1 | 9 | 526aa/60.1kDa，理想实验范围 |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=73 (61-80→4) |
| 三维结构 | 9/10 | ×3 | 27 | pLDDT=91.6, pct>90=81.4%；高质量预测 |
| 调控结构域 | 3/10 | ×2 | 6 | IPR004856 (Glycosyl transferase ALG8)，单一糖基转移酶域 |
| PPI网络 | 5/10 | ×3 | 15 | ALG6(0.999实验), ALG10B(0.966); N-糖基化通路 |
| **加权总分** | | | **89/180** | |
| **归一化总分 (÷1.8)** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm (main) | Approved |
| UniProt | Endoplasmic reticulum membrane | |
| GO-CC | GO:0005789 (ER membrane, IGI), GO:0098553 (lumenal side of ER membrane, IC) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。显著矛盾：HPA Approved IF 显示 Nucleoplasm，但 UniProt/GO-CC 均为 ER 膜腔侧蛋白。ALG8 作为 N-糖基化途径的葡萄糖基转移酶，功能明确在 ER 腔面。**评分: 3/10**。

#### 3.2 蛋白大小评估

526 aa / 60.1 kDa。理想实验范围，大小适中，结构预测质量高。**评分: 9/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 73 |
| PubMed symbol_only | 111 |
| 主要方向 | 多囊肾病、先天性糖基化疾病、ALG8-CDG |

**评价**: PubMed 73 篇 (strict)，研究热度中等偏高。ALG8 在多囊肾病遗传学和 ALG8-CDG 中有较多临床遗传学研究。新颖度偏低。**评分: 4/10** (61-80篇)。

**关键文献**:
1. Cornec-Le Gall E et al. (2018). "Genetic Complexity of Autosomal Dominant Polycystic Kidney and Liver Diseases." *J Am Soc Nephrol*. PMID: 29038287
2. Chang AR et al. (2022). "Exome Sequencing of a Clinical Population for Autosomal Dominant Polycystic Kidney Disease." *JAMA*. PMID: 36573973
3. Jawaid T et al. (2025). "Characterization of the Cystic Phenotype Associated with Monoallelic ALG8 and ALG9 Pathogenic Variants." *J Am Soc Nephrol*. PMID: 39899384
4. Albokhari D et al. (2022). "ALG8-CDG: Molecular and phenotypic expansion suggests clinical management guidelines." *J Inherit Metab Dis*. PMID: 35716054
5. Mantovani V et al. (2020). "Gene Panel Analysis in a Large Cohort of Patients With Autosomal Dominant Polycystic Kidney Disease." *Front Genet*. PMID: 32457805

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 91.6 |
| pLDDT > 90 (Very High) | 81.4% |
| pLDDT 70-90 (High) | 11.2% |
| pLDDT 50-70 (Medium) | 3.2% |
| pLDDT < 50 (Low) | 4.2% |
| 有序区域 (pLDDT>70) | 92.6% |
| 实验结构 (PDB) | 无 |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。AlphaFold 极高质量预测 (pLDDT 91.6)。**评分: 9/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR004856 (Glycosyl transferase, ALG8) |
| Pfam | PF03155 (ALG8 glycosyltransferase) |

单一糖基转移酶结构域，催化 Dol-P-Glc 向脂联寡糖中间体添加第二葡萄糖残基。无转录调控或染色质相关结构域。**评分: 3/10**。

#### 3.6 PPI 网络

| Partner | Score | 实验证据 |
|---------|-------|---------|
| ALG6 | 0.999 | 0.98 (强实验证据) |
| ALG10B | 0.966 | 0.074 |
| ALG10 | 0.965 | 0.067 |
| ALG3 | 0.882 | 0.109 |
| ALG12 | 0.878 | 0.069 |

PPI 集中于 N-糖基化途径，ALG6 有极强实验互作证据 (0.98)。IntAct 确认 ALG6 co-IP。通路专一性极强。**评分: 5/10**。

### 4. 拒绝理由

ALG8 nuclear_score=3 (≤3 阈值)，核心原因：
- HPA Nucleoplasm 与 UniProt ER 膜定位根本矛盾
- 功能为 ER 腔面葡萄糖基转移酶，无核功能
- PubMed 73 篇 (>60)，研究热度偏高
- 结构域单一，仅含糖基转移酶

**结论**: 虽 AlphaFold 质量极佳，但定位矛盾根本、功能非核、研究热度高，不符合核蛋白筛选标准。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BVK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BVK2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ALG8%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000159063-ALG8
