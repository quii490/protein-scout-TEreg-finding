---
type: protein-evaluation
gene: "Smn1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## Smn1 — REJECTED (研究热度过高 (PubMed strict=1608，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Smn1 / SMN, SMNT |
| 蛋白名称 | Survival motor neuron protein |
| 蛋白大小 | 294 aa / 31.8 kDa |
| UniProt ID | Q16637 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies, Cytosol; UniProt: Nucleus, gem; Nucleus, Cajal body; Cytoplasm; Cytoplasmic gr |
| 蛋白大小 | 10/10 | ×1 | 10 | 294 aa / 31.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1608 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.9; PDB: 1G5V, 1MHN, 2LEH, 4A4E, 4A4G, 4GLI, 4QQ6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040424, IPR047313, IPR049481, IPR010304, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Cytosol | Supported |
| UniProt | Nucleus, gem; Nucleus, Cajal body; Cytoplasm; Cytoplasmic granule; Perikaryon; Cell projection, neur... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon (GO:0030424)
- Cajal body (GO:0015030)
- cytoplasm (GO:0005737)
- cytoplasmic ribonucleoprotein granule (GO:0036464)
- cytosol (GO:0005829)
- Gemini of Cajal bodies (GO:0097504)
- neuron projection (GO:0043005)
- nuclear body (GO:0016604)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1608 |
| PubMed broad count | 2004 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SMN, SMNT |

**关键文献**:
1. Spinal Muscular Atrophy.. *Neurologic clinics*. PMID: 26515624
2. Spinal Muscular Atrophy: The Past, Present, and Future of Diagnosis and Treatment.. *International journal of molecular sciences*. PMID: 37569314
3. Spinal muscular atrophy.. *Lancet (London, England)*. PMID: 18572081
4. Gene Therapy for Spinal Muscular Atrophy (SMA): A Review of Current Challenges and Safety Considerations for Onasemnogene Abeparvovec (Zolgensma).. *Cureus*. PMID: 37065340
5. Onasemnogene Abeparvovec: A Review in Spinal Muscular Atrophy.. *CNS drugs*. PMID: 35960489

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.9 |
| 高置信度残基 (pLDDT>90) 占比 | 24.5% |
| 置信残基 (pLDDT 70-90) 占比 | 17.0% |
| 中等置信 (pLDDT 50-70) 占比 | 31.0% |
| 低置信 (pLDDT<50) 占比 | 27.6% |
| 有序区域 (pLDDT>70) 占比 | 41.5% |
| 可用 PDB 条目 | 1G5V, 1MHN, 2LEH, 4A4E, 4A4G, 4GLI, 4QQ6, 5XJL, 5XJQ, 5XJR |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.9），有序残基占 41.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040424, IPR047313, IPR049481, IPR010304, IPR002999; Pfam: PF20636, PF06003, PF20635 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SNRPD1 | 0.999 | 0.984 | — |
| GEMIN2 | 0.999 | 0.992 | — |
| SNRPD2 | 0.998 | 0.979 | — |
| DDX20 | 0.998 | 0.954 | — |
| STRAP | 0.998 | 0.878 | — |
| SNRPE | 0.998 | 0.963 | — |
| SNRPG | 0.997 | 0.963 | — |
| SNRPF | 0.997 | 0.965 | — |
| GEMIN4 | 0.995 | 0.873 | — |
| GEMIN7 | 0.994 | 0.847 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMN2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Vav2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| MED19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED26 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| KPNB1 | psi-mi:"MI:0096"(pull down) | pubmed:15494309 |
| SNRPB | psi-mi:"MI:0096"(pull down) | pubmed:15494309 |
| POP7 | psi-mi:"MI:0096"(pull down) | pubmed:14715275 |
| Rpp20 | psi-mi:"MI:0096"(pull down) | pubmed:14715275 |
| RNPS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.9 + PDB: 1G5V, 1MHN, 2LEH, 4A4E, 4A4G,  | pLDDT=66.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, gem; Nucleus, Cajal body; Cytoplasm; Cyto / Nuclear bodies, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. Smn1 — Survival motor neuron protein，研究基础较多，新颖性有限。
2. 蛋白大小294 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1608 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1608 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16637
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172062-SMN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Smn1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16637
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
