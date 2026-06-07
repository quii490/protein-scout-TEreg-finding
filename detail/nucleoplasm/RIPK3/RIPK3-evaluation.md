---
type: protein-evaluation
gene: "RIPK3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RIPK3 — REJECTED (研究热度过高 (PubMed strict=1616，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RIPK3 / RIP3 |
| 蛋白名称 | Receptor-interacting serine/threonine-protein kinase 3 |
| 蛋白大小 | 518 aa / 56.9 kDa |
| UniProt ID | Q9Y572 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytosol; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 518 aa / 56.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1616 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.1; PDB: 5V7Z, 5ZCK, 7DA4, 7DAC, 7MON, 7MX3, 8Z94 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR000719, IPR017441, IPR025735, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.0/180** | |
| **归一化总分** | | | **45.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)
- ripoptosome (GO:0097342)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1616 |
| PubMed broad count | 2948 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RIP3 |

**关键文献**:
1. ZBP1 mediates interferon-induced necroptosis.. *Cellular & molecular immunology*. PMID: 31076724
2. Extracellular RIPK3 Acts as a Damage-Associated Molecular Pattern to Exaggerate Cardiac Ischemia/Reperfusion Injury.. *Circulation*. PMID: 39411860
3. RIPK3 dampens mitochondrial bioenergetics and lipid droplet dynamics in metabolic liver disease.. *Hepatology (Baltimore, Md.)*. PMID: 36029129
4. Ripks and Neuroinflammation.. *Molecular neurobiology*. PMID: 38349514
5. Sensing of mitochondrial DNA by ZBP1 promotes RIPK3-mediated necroptosis and ferroptosis in response to diquat poisoning.. *Cell death and differentiation*. PMID: 38493248

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.1 |
| 高置信度残基 (pLDDT>90) 占比 | 40.5% |
| 置信残基 (pLDDT 70-90) 占比 | 13.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 43.4% |
| 有序区域 (pLDDT>70) 占比 | 54.0% |
| 可用 PDB 条目 | 5V7Z, 5ZCK, 7DA4, 7DAC, 7MON, 7MX3, 8Z94, 9LFU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.1），有序残基占 54.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR017441, IPR025735, IPR008271; Pfam: PF00069, PF12721 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRADD | 0.999 | 0.052 | — |
| RIPK1 | 0.999 | 0.999 | — |
| MLKL | 0.999 | 0.999 | — |
| CASP8 | 0.999 | 0.994 | — |
| FADD | 0.999 | 0.994 | — |
| TNF | 0.998 | 0.994 | — |
| ZBP1 | 0.996 | 0.292 | — |
| CFLAR | 0.992 | 0.067 | — |
| TICAM1 | 0.983 | 0.345 | — |
| BIRC2 | 0.976 | 0.329 | — |

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
| 三维结构 | AlphaFold pLDDT=67.1 + PDB: 5V7Z, 5ZCK, 7DA4, 7DAC, 7MON,  | pLDDT=67.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. RIPK3 — Receptor-interacting serine/threonine-protein kinase 3，研究基础较多，新颖性有限。
2. 蛋白大小518 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1616 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1616 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y572
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129465-RIPK3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RIPK3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y572
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y572-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y572 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 21..287; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR011009;IPR000719;IPR017441;IPR025735;IPR008271;IPR051681; |
| Pfam | PF00069;PF12721; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000129465-RIPK3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BIRC2 | Intact, Biogrid | true |
| BIRC3 | Intact, Biogrid | true |
| CASP8 | Intact, Biogrid | true |
| MLKL | Intact, Biogrid | true |
| RIPK1 | Intact, Biogrid | true |
| DAXX | Biogrid | false |
| FADD | Biogrid | false |
| PELI1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
