---
type: protein-evaluation
gene: "FEZ2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FEZ2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FEZ2 |
| 蛋白名称 | Fasciculation and elongation protein zeta-2 |
| 蛋白大小 | 353 aa / 39.7 kDa |
| UniProt ID | Q9UHY8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli, Nucleoli rim; 额外: Golgi apparatus, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 353 aa / 39.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011680; Pfam: PF07763 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim; 额外: Golgi apparatus, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon (GO:0030424)
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. FEZ2 has acquired additional protein interaction partners relative to FEZ1: functional and evolutionary implications.. *PloS one*. PMID: 21408165
2. Fasciculation and elongation zeta proteins 1 and 2: From structural flexibility to functional diversity.. *World journal of biological chemistry*. PMID: 30815230
3. Identification of FEZ2 as a potential oncogene in pancreatic ductal adenocarcinoma.. *PeerJ*. PMID: 35036176
4. FEZ1 dimerization and interaction with transcription regulatory proteins involves its coiled-coil region.. *The Journal of biological chemistry*. PMID: 16484223
5. Identification of a tissue-non-specific homologue of axonal fasciculation and elongation protein zeta-1.. *Biochemical and biophysical research communications*. PMID: 14697253

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.7 |
| 高置信度残基 (pLDDT>90) 占比 | 22.4% |
| 置信残基 (pLDDT 70-90) 占比 | 35.1% |
| 中等置信 (pLDDT 50-70) 占比 | 20.1% |
| 低置信 (pLDDT<50) 占比 | 22.4% |
| 有序区域 (pLDDT>70) 占比 | 57.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=70.7，有序区 57.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011680; Pfam: PF07763 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CRIM1 | 0.894 | 0.000 | — |
| SCOC | 0.887 | 0.716 | — |
| LZTS1 | 0.794 | 0.000 | — |
| ATF5 | 0.668 | 0.000 | — |
| PRKCZ | 0.651 | 0.292 | — |
| KIF6 | 0.617 | 0.591 | — |
| NEK1 | 0.604 | 0.292 | — |
| C20orf194 | 0.583 | 0.000 | — |
| TBC1D19 | 0.563 | 0.000 | — |
| RAB11FIP2 | 0.525 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.7 + PDB: 无 | pLDDT=70.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli, Nucleoli rim; 额外: Golgi apparatus, Cytos | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FEZ2 — Fasciculation and elongation protein zeta-2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小353 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UHY8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171055-FEZ2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FEZ2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UHY8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
