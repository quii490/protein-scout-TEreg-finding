---
type: protein-evaluation
gene: "NCKIPSD"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NCKIPSD 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NCKIPSD / AF3P21, SPIN90 |
| 蛋白名称 | NCK-interacting protein with SH3 domain |
| 蛋白大小 | 722 aa / 79.0 kDa |
| UniProt ID | Q9NZQ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 722 aa / 79.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=75.2; PDB: 6DEC, 6DED, 6DEE, 9I2B, 9M5E, 9M64 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036028, IPR001452, IPR030125, IPR018556, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **144.0/180** | |
| **归一化总分** | | | **80.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- glutamatergic synapse (GO:0098978)
- intermediate filament (GO:0005882)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- postsynapse (GO:0098794)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AF3P21, SPIN90 |

**关键文献**:
1. Genome-Wide Analysis of Protein-Coding Variants in Leprosy.. *The Journal of investigative dermatology*. PMID: 28842327
2. Transgelin interacts with PARP1 in human colon cancer cells.. *Cancer cell international*. PMID: 32774160
3. Bridging the gap: Short structural variants in the genetics of anorexia nervosa.. *The International journal of eating disorders*. PMID: 35470453
4. Protein and phosphoprotein levels in glioma and adenocarcinoma cell lines grown in normoxia and hypoxia in monolayer and three-dimensional cultures.. *Proteome science*. PMID: 22276931
5. Identification and Functional Analysis of Ras-Related Associated with Diabetes Gene (rrad) in Edwardsiella piscicida-Resistant Individuals of Japanese Flounder (Paralichthys olivaceus).. *International journal of molecular sciences*. PMID: 39408905

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.2 |
| 高置信度残基 (pLDDT>90) 占比 | 48.2% |
| 置信残基 (pLDDT 70-90) 占比 | 20.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 28.0% |
| 有序区域 (pLDDT>70) 占比 | 68.4% |
| 可用 PDB 条目 | 6DEC, 6DED, 6DEE, 9I2B, 9M5E, 9M64 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6DEC, 6DED, 6DEE, 9I2B, 9M5E, 9M64）+ AlphaFold极高置信度预测（pLDDT=75.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036028, IPR001452, IPR030125, IPR018556, IPR035514; Pfam: PF00018, PF09431 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NCK1 | 0.995 | 0.620 | — |
| ARPC5 | 0.987 | 0.967 | — |
| ARPC4 | 0.984 | 0.967 | — |
| ARPC2 | 0.976 | 0.941 | — |
| ARPC3 | 0.974 | 0.940 | — |
| ACTR3 | 0.972 | 0.941 | — |
| ACTR2 | 0.971 | 0.928 | — |
| WAS | 0.919 | 0.079 | — |
| ARPC1B | 0.910 | 0.826 | — |
| BAIAP2 | 0.907 | 0.693 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BAIAP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NCK2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18850735|imex:IM-20477 |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FASLG | psi-mi:"MI:0084"(phage display) | pubmed:19807924|imex:IM-20398 |
| GRB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19380743|imex:IM-20432 |
| Crkl | psi-mi:"MI:0096"(pull down) | imex:IM-8314|pubmed:20697350|m |
| STAC | psi-mi:"MI:0018"(two hybrid) | imex:IM-13772|pubmed:18654987 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.2 + PDB: 6DEC, 6DED, 6DEE, 9I2B, 9M5E,  | pLDDT=75.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NCKIPSD — NCK-interacting protein with SH3 domain，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小722 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZQ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213672-NCKIPSD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NCKIPSD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZQ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
