---
type: protein-evaluation
gene: "DNAJC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC1 / HTJ1 |
| 蛋白名称 | DnaJ homolog subfamily C member 1 |
| 蛋白大小 | 554 aa / 63.9 kDa |
| UniProt ID | Q96KC8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum; UniProt: Endoplasmic reticulum membrane; Nucleus membrane; Microsome  |
| 蛋白大小 | 10/10 | ×1 | 10 | 554 aa / 63.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=70.8; PDB: 2CQQ, 2CQR |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001623, IPR018253, IPR052606, IPR009057, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.5/180** | |
| **归一化总分** | | | **77.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum | Approved |
| UniProt | Endoplasmic reticulum membrane; Nucleus membrane; Microsome membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endomembrane system (GO:0012505)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- nuclear membrane (GO:0031965)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HTJ1 |

**关键文献**:
1. A naturally occurring canine model of syndromic congenital microphthalmia.. *G3 (Bethesda, Md.)*. PMID: 38682429
2. DNAJ heat shock protein family member C1 can regulate proliferation and migration in hepatocellular carcinoma.. *PeerJ*. PMID: 37520264
3. Grp78 destabilization of infectious prions is strain-specific and modified by multiple factors including accessory chaperones and pH.. *The Journal of biological chemistry*. PMID: 38718859
4. Epigenetic adaptations of the masticatory mucosa to periodontal inflammation.. *Clinical epigenetics*. PMID: 34732256
5. Single-Cell Gene Network Analysis and Transcriptional Landscape of MYCN-Amplified Neuroblastoma Cell Lines.. *Biomolecules*. PMID: 33525507

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.8 |
| 高置信度残基 (pLDDT>90) 占比 | 29.1% |
| 置信残基 (pLDDT 70-90) 占比 | 29.4% |
| 中等置信 (pLDDT 50-70) 占比 | 13.9% |
| 低置信 (pLDDT<50) 占比 | 27.6% |
| 有序区域 (pLDDT>70) 占比 | 58.5% |
| 可用 PDB 条目 | 2CQQ, 2CQR |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2CQQ, 2CQR）+ AlphaFold高质量预测（pLDDT=70.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001623, IPR018253, IPR052606, IPR009057, IPR036869; Pfam: PF00226, PF23082 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA5 | 0.987 | 0.693 | — |
| SERPINA3 | 0.812 | 0.292 | — |
| CTRB2 | 0.767 | 0.000 | — |
| CTRB1 | 0.754 | 0.000 | — |
| SEC63 | 0.724 | 0.221 | — |
| HSPA8 | 0.676 | 0.514 | — |
| DNAJC3 | 0.662 | 0.396 | — |
| HSPA12A | 0.580 | 0.274 | — |
| HSPA9 | 0.569 | 0.413 | — |
| HSPA4 | 0.569 | 0.274 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.8 + PDB: 2CQQ, 2CQR | pLDDT=70.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus membrane;  / Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DNAJC1 — DnaJ homolog subfamily C member 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小554 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96KC8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136770-DNAJC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96KC8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
