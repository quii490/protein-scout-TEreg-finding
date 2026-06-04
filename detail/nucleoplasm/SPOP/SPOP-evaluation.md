---
type: protein-evaluation
gene: "Spop"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## Spop — REJECTED (研究热度过高 (PubMed strict=438，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Spop |
| 蛋白名称 | Speckle-type POZ protein |
| 蛋白大小 | 374 aa / 42.1 kDa |
| UniProt ID | O43791 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Nucleus speckle; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 374 aa / 42.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=438 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=90.1; PDB: 2CR2, 3HQH, 3HQI, 3HQL, 3HQM, 3HSV, 3HTM |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR056423, IPR000210, IPR002083, IPR011333, IPR034 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Nucleus speckle; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- cytoplasm (GO:0005737)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 438 |
| PubMed broad count | 668 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Deregulation of SPOP in Cancer.. *Cancer research*. PMID: 36512624
2. The Molecular Taxonomy of Primary Prostate Cancer.. *Cell*. PMID: 26544944
3. Phosphorylation regulates cullin-based ubiquitination in tumorigenesis.. *Acta pharmaceutica Sinica. B*. PMID: 33643814
4. SPOP mutations promote p62/SQSTM1-dependent autophagy and Nrf2 activation in prostate cancer.. *Cell death and differentiation*. PMID: 34987184
5. CSN6-SPOP-HMGCS1 Axis Promotes Hepatocellular Carcinoma Progression via YAP1 Activation.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38308184

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.1 |
| 高置信度残基 (pLDDT>90) 占比 | 77.3% |
| 置信残基 (pLDDT 70-90) 占比 | 11.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 4.3% |
| 有序区域 (pLDDT>70) 占比 | 88.8% |
| 可用 PDB 条目 | 2CR2, 3HQH, 3HQI, 3HQL, 3HQM, 3HSV, 3HTM, 3HU6, 3IVB, 3IVQ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2CR2, 3HQH, 3HQI, 3HQL, 3HQM, 3HSV, 3HTM, 3HU6, 3IVB, 3IVQ）+ AlphaFold极高置信度预测（pLDDT=90.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR056423, IPR000210, IPR002083, IPR011333, IPR034089; Pfam: PF24570, PF00651, PF22486 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.999 | 0.997 | — |
| RBX1 | 0.996 | 0.091 | — |
| GLI3 | 0.994 | 0.877 | — |
| GLI2 | 0.991 | 0.726 | — |
| GLI1 | 0.990 | 0.296 | — |
| PTEN | 0.990 | 0.972 | — |
| DAXX | 0.974 | 0.798 | — |
| PDX1 | 0.972 | 0.971 | — |
| SPOPL | 0.966 | 0.469 | — |
| SUFU | 0.960 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000499562.1 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| RXRB | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DDIT3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RTN3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MYD88 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DPPA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZBTB16 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GDI1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| KPNA6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PIP5K1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.1 + PDB: 2CR2, 3HQH, 3HQI, 3HQL, 3HQM,  | pLDDT=90.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle; Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. Spop — Speckle-type POZ protein，研究基础较多，新颖性有限。
2. 蛋白大小374 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 438 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 438 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43791
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121067-SPOP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Spop
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43791
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
