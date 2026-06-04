---
type: protein-evaluation
gene: "GP5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GP5 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=554，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GP5 |
| 蛋白名称 | Platelet glycoprotein V |
| 蛋白大小 | 560 aa / 61.0 kDa |
| UniProt ID | P40197 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 560 aa / 61.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=554 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000483, IPR001611, IPR003591, IPR050467, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **68.5/180** | |
| **归一化总分** | | | **38.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- glycoprotein Ib-IX-V complex (GO:1990779)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 554 |
| PubMed broad count | 1381 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. PRRSV, the virus.. *Veterinary research*. PMID: 10726635
2. Development of a Ferritin Protein Nanoparticle Vaccine with PRRSV GP5 Protein.. *Viruses*. PMID: 38932282
3. Nanoparticle Vaccine Triggers Interferon-Gamma Production and Confers Protective Immunity against Porcine Reproductive and Respiratory Syndrome Virus.. *ACS nano*. PMID: 39757928
4. The mRNA vaccine expressing fused structural protein of PRRSV protects piglets against PRRSV challenge.. *Veterinary microbiology*. PMID: 40318244
5. Replacing the decoy epitope of PCV2 capsid protein with epitopes of GP3 and/or GP5 of PRRSV enhances the immunogenicity of bivalent vaccines in mice.. *Journal of virological methods*. PMID: 32650038

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.5 |
| 高置信度残基 (pLDDT>90) 占比 | 71.2% |
| 置信残基 (pLDDT 70-90) 占比 | 13.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 11.8% |
| 有序区域 (pLDDT>70) 占比 | 85.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.5，有序区 85.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000483, IPR001611, IPR003591, IPR050467, IPR032675; Pfam: PF13855, PF01463 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GP9 | 0.999 | 0.292 | — |
| VWF | 0.996 | 0.100 | — |
| GP1BB | 0.996 | 0.000 | — |
| CD151 | 0.994 | 0.000 | — |
| CD36 | 0.991 | 0.000 | — |
| GP1BA | 0.979 | 0.292 | — |
| GP6 | 0.961 | 0.095 | — |
| TXN | 0.958 | 0.098 | — |
| GTPBP1 | 0.950 | 0.000 | — |
| SIGLEC1 | 0.949 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| 27 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15701513 |
| GP9 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-24277|pubmed:1730602 |
| RAET1L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SLC19A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| IGSF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RTN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ARL6IP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RHOBTB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TOMM40 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ATP5MC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.5 + PDB: 无 | pLDDT=86.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GP5 — Platelet glycoprotein V，研究基础较多，新颖性有限。
2. 蛋白大小560 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 554 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P40197
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178732-GP5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GP5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P40197
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
