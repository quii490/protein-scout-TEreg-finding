---
type: protein-evaluation
gene: "CASD1"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CASD1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CASD1 / C7orf12 |
| 蛋白全名 | N-acetylneuraminate (7)9-O-acetyltransferase |
| 蛋白大小 | 797 aa / 91.7 kDa |
| UniProt ID | Q96PB1 |
| 子定位分类 | nucleoplasm |
| HPA IF 主定位 | Nucleoplasm |
| HPA IF 附加定位 | 无 |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28 | HPA主定位核 |
| 蛋白大小 | 10/10 | x1 | 10 | 797 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=17 (Extremely novel) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold高质量(pLDDT=87.8, >70%=93.1%) |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 4/10 | x3 | 12 | STRING综合分>0.7 (1条)，主要为预测 |
| 互证加分 | — | max+3 | +0.5 | InterPro注释丰富(3个结构域) (+0.5) |
| **加权总分** | | | **138.5/180** | |
| **归一化总分 (÷1.83)** | | | **75.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm | Approved |
| UniProt | Golgi apparatus membrane (ECO:0000269) | Swiss-Prot/TrEMBL |
| GO-CC | Golgi membrane (IDA:UniProtKB) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA主定位核

#### 3.2 蛋白大小评估

797 aa (200-800 aa ideal range)

**评价**: 797 aa / 91.7 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 17 |
| PubMed symbol_only | 23 |
| PubMed broad | 24 |
| 别名 | C7orf12 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 17 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **Loss of sialic acid side-chain O-acetylation exacerbates colitis.** *Proceedings of the National Academy of Sciences of the United States of America* (2025 Aug 26) PMID:40828018 -- Ji Y et al.
2. **The human Cas1 protein: a sialic acid-specific O-acetyltransferase?** *Glycobiology* (2011 May) PMID:20947662 -- Arming S et al.
3. **O-acetylated Gangliosides as Targets for Cancer Immunotherapy.** *Cells* (2020 Mar 17) PMID:32192217 -- Cavdarli S et al.
4. **Expression of 9-O- and 7,9-O-Acetyl Modified Sialic Acid in Cells and Their Effects on Influenza Viruses.** *mBio* (2019 Dec 3) PMID:31796537 -- Barnard KN et al.
5. **Ectopic expression of Capsicum-specific cell wall protein Capsicum annuum senescence-delaying 1 (CaSD1) delays senescence and induces trichome formation in Nicotiana benthamiana.** *Molecules and cells* (2012 Apr) PMID:22441673 -- Seo E et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 87.8 |
| pLDDT > 90 (Very High) | 58.7% |
| pLDDT 70-90 (High) | 34.4% |
| pLDDT 50-70 (Medium) | 4.3% |
| pLDDT < 50 (Low) | 2.6% |
| 有序区域 (pLDDT>70) 占比 | 93.1% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 高质量预测（pLDDT=87.8，有序区域 93%）。

**评分: 8/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | 无注释 |
| Pfam | 无注释 |

**染色质调控潜力分析**: 存在注释结构域（0个），但未发现明确染色质/DNA结合域。新颖蛋白基线不扣分。

**评分: 7/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4, top 10):

| Partner | Score | 实验分 | 调控相关? |
|---------|-------|--------|----------|
| SIAE | 0.795 | 0.000 | — |
| BTNL3 | 0.599 | 0.000 | — |
| ST8SIA1 | 0.597 | 0.000 | — |
| NEU4 | 0.568 | 0.000 | — |
| PPP1R9A | 0.551 | 0.000 | — |
| SGCE | 0.540 | 0.000 | — |
| ST3GAL5 | 0.518 | 0.000 | — |
| ASB4 | 0.502 | 0.000 | — |
| ST6GAL1 | 0.472 | 0.000 | — |
| ST6GALNAC1 | 0.471 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| NDUFB3 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |
| COX6B1 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |


**已知复合体成员** (GO Cellular Component):
- Golgi membrane (IDA:UniProtKB)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 2
- 调控相关比例: 0/15 (0%)

**评价**: STRING综合分>0.7 (1条)，主要为预测

**评分: 4/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 2 | 数据充分 |

**互证加分明细**:
- InterPro注释丰富(3个结构域) (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (75.7/100)

**核心优势**:
1. Extremely novel -- PubMed=17篇
2. HPA主定位核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96PB1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CASD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96PB1
- STRING: https://string-db.org/cgi/network?identifiers=CASD1&species=9606

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96PB1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR012419;IPR036915;IPR057106; |
| Pfam | PF07779;PF24536; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000127995-CASD1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
