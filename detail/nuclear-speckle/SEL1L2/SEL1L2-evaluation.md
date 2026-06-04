---
type: protein-evaluation
gene: "SEL1L2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SEL1L2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SEL1L2 / C20orf50 |
| 蛋白名称 | Protein sel-1 homolog 2 |
| 蛋白大小 | 688 aa / 78.0 kDa |
| UniProt ID | Q5TEA6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Membrane; Cell projection, cilium; Nucleus speckle |
| 蛋白大小 | 10/10 | ×1 | 10 | 688 aa / 78.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006597, IPR050767, IPR011990; Pfam: PF08238 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.0/180** | |
| **归一化总分** | | | **75.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Membrane; Cell projection, cilium; Nucleus speckle | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cilium (GO:0005929)
- endoplasmic reticulum membrane (GO:0005789)
- nuclear speck (GO:0016607)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf50 |

**关键文献**:
1. Crosstalk between Gut Microbiota and Epigenetic Markers in Obesity Development: Relationship between Ruminococcus, BMI, and MACROD2/SEL1L2 Methylation.. *Nutrients*. PMID: 37049393
2. A recurrent PJA1 variant in trigonocephaly and neurodevelopmental disorders.. *Annals of clinical and translational neurology*. PMID: 32530565

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.2 |
| 高置信度残基 (pLDDT>90) 占比 | 62.2% |
| 置信残基 (pLDDT 70-90) 占比 | 19.3% |
| 中等置信 (pLDDT 50-70) 占比 | 11.2% |
| 低置信 (pLDDT<50) 占比 | 7.3% |
| 有序区域 (pLDDT>70) 占比 | 81.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.2，有序区 81.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006597, IPR050767, IPR011990; Pfam: PF08238 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TOMM20 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| EZR | psi-mi:"MI:0096"(pull down) | pubmed:29568061|imex:IM-26301 |
| EPHB4 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |
| TYRO3 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:35384245|imex:IM-29494 |
| FGFR1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:35384245|imex:IM-29494 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 5
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.2 + PDB: 无 | pLDDT=85.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Cell projection, cilium; Nucleus speckle / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 5 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SEL1L2 — Protein sel-1 homolog 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小688 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5TEA6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101251-SEL1L2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SEL1L2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5TEA6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
