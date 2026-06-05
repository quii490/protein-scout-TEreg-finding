---
type: protein-evaluation
gene: "AMER1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AMER1 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AMER1 / FAM123B / WTX |
| 蛋白大小 | 1135 aa / 124.0 kDa |
| UniProt ID | Q5JTC6 |
| 蛋白全名 | APC membrane recruitment protein 1 |
| 子定位分类 | nuclear-body |
| HPA IF 主定位 | Nuclear bodies |
| HPA IF 附加定位 | Vesicles, Plasma membrane |
| HPA Reliability | Supported |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24 | HPA主定位Nuclear bodies；UniProt Cell membrane/Cytoplasm/Nucleus；核体定位明确 |
| 蛋白大小 | 6/10 | ×1 | 6 | 1135aa/124.0kDa，大蛋白，重组表达困难 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=53 (41-60→6) |
| 三维结构 | 3/10 | ×3 | 9 | pLDDT=48.3, pct<50=72.2%；高度无序 |
| 调控结构域 | 7/10 | ×2 | 14 | IPR019003 WTX family；Wnt/β-catenin调控，APC/AXIN/CTNNB1核心伙伴 |
| PPI网络 | 8/10 | ×3 | 24 | AXIN1(0.999实验), APC(0.998实验), CTNNB1(0.992实验)；Wnt核心网络 |
| **加权总分** | | | **107/180**** | |
| **归一化总分 (÷1.83)** | | | **58.5/100**** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nuclear bodies (main), Vesicles (additional), Plasma membrane (additional) | Supported |
| UniProt | Cell membrane, Cytoplasm, Nucleus | |
| GO-CC | GO:0016604 (nuclear body, IDA:HPA), GO:0005886 (plasma membrane, IDA:HPA), GO:0005829 (cytosol, TAS) | |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

#### 3.2 蛋白大小评估

1135 aa / 124.0 kDa。大蛋白，超过 800 aa 理想范围。高度无序 (72.2% pLDDT<50)，重组全长表达困难。需截短体策略。**评分: 6/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 53 |
| PubMed symbol_only | 82 |
| 别名 | FAM123B, WTX |
| 主要方向 | Wnt信号、Wilms肿瘤、结直肠癌、骨硬化症 |

**评价**: PubMed 53 篇 (strict)，中等研究热度。AMER1/WTX 作为 Wnt/β-catenin 信号通路关键调控因子，在肿瘤生物学中有较多研究。**评分: 6/10** (41-60篇)。

**关键文献**:
1. Boutet A et al. (2010). "The WTX/AMER1 gene family: evolution, signature and function." *BMC Evol Biol*. PMID: 20843316 — 家族进化与功能综述
2. Palles C et al. (2022). "Germline MBD4 deficiency causes a multi-tumor predisposition syndrome." *Am J Hum Genet*. PMID: 35460607
3. Guo L et al. (2023). "Molecular Profiling Provides Clinical Insights Into Targeted and Immunotherapies as Well as Colorectal Cancer Prognosis." *Gastroenterology*. PMID: 37146911
4. Brunet Guasch M et al. (2025). "Mathematical Modeling Quantifies 'Just-Right' APC Inactivation for Colorectal Cancer Initiation." *Cancer Res*. PMID: 41091816
5. Adam MP et al. (1993/updated). "Osteopathia Striata with Cranial Sclerosis." *GeneReviews*. PMID: 33856753

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 48.3 |
| pLDDT > 90 (Very High) | 6.8% |
| pLDDT 70-90 (High) | 2.6% |
| pLDDT 50-70 (Medium) | 18.4% |
| pLDDT < 50 (Low) | 72.2% |
| 有序区域 (pLDDT>70) | 9.4% |
| 实验结构 (PDB) | 4YJE (X-ray 1.90A, B=325-335); 4YJL (2.10A, G-L=496-508); 4YK6 (1.70A, B=365-375) — 仅短肽片段 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR019003 (WTX/AMER1 family) |
| Pfam | PF09422 (WTX family) |

AMER1 为 WTX/AMER1 家族成员，含多个短线性基序 (SLiMs) 介导特定蛋白-蛋白互作。作为 Wnt/β-catenin 破坏复合体的支架蛋白，通过对 PtdIns(4,5)P2 的膜结合将 APC/AXIN/GSK3B/CTNNB1 招募至细胞膜。同时调控 β-catenin 泛素化和降解。核心 Wnt 信号调控因子。**评分: 7/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (top 10):

| Partner | Score | 实验证据 | 功能 |
|---------|-------|---------|------|
| AXIN1 | 0.999 | 0.80 | β-catenin破坏复合体核心 |
| APC | 0.998 | 0.971 | β-catenin破坏复合体核心 |
| GSK3B | 0.993 | 0 | Wnt激酶 |
| CTNNB1 | 0.992 | 0.783 | Wnt效应器, 实验互作 |
| KEAP1 | 0.978 | 0.629 | 氧化应激/NRF2 |
| CSNK1A1 | 0.960 | 0 | Wnt激酶 |
| BTRC | 0.952 | 0.615 | E3泛素连接酶 |
| WT1 | 0.849 | 0 | Wilms肿瘤 |
| DVL1 | 0.788 | 0 | Wnt信号 |
| FBXW11 | 0.788 | 0.733 | E3泛素连接酶 |

**UniProt 实验互作**: AXIN1 (7实验), CTNNB1 (9实验), BTRC (7实验), FBXW11 (6实验), APC (4实验), KEAP1 (2实验), AMER3 (4实验)

**PPI 互证分析**: PPI 网络为所有评估基因中最强之一。核心 Wnt/β-catenin 破坏复合体成员全覆盖 (AXIN1, APC, GSK3B, CTNNB1, CSNK1A1, BTRC)。AXIN1、APC、CTNNB1 均有强实验证据 (0.80-0.97)。KEAP1 互作使 NRF2 氧化应激通路与 Wnt 信号交叉。**评分: 8/10**。

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5) — 59.4/100

**核心优势**:
1. Wnt/β-catenin 核心调控因子，信号通路重要性极高
2. PPI 网络极强，覆盖完整破坏复合体
3. HPA Nuclear bodies 主定位
4. 与 APC/AXIN/CTNNB1/GSK3B 所有核心伙伴的实验互作
5. 肿瘤生物学高度相关

**风险/不确定性**:
1. 蛋白高度无序 (72.2% pLDDT<50)，结构研究困难
2. 大蛋白 (1135 aa)，重组表达困难
3. PubMed 53 篇 (>40)，新颖度中等
4. 无序蛋白的生化/结构实验设计挑战大

**下一步建议**:
- [ ] 利用已解析的短肽-β-catenin/Axin 结构设计截短体
- [ ] 探索 AMER1 的液-液相分离行为（IDR占主导）
- [ ] 在 TEreg 背景下验证 AMER1 的 Wnt 信号调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JTC6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JTC6
- PDB: https://www.rcsb.org/structure/4YJE
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AMER1%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000184675-AMER1
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000184675-AMER1/subcellular

![](https://images.proteinatlas.org/65265/1151_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/65265/1151_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/65265/1154_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/65265/1154_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/65265/1254_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/65265/1254_F7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5JTC6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
