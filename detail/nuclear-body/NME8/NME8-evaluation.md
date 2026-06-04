---
type: protein-evaluation
gene: "NME8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, recovery, re-evaluation]
status: scored
---

## NME8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NME8 / SPTRX2, TXNDC3 |
| 蛋白名称 | Protein NME8 |
| 蛋白大小 | 588 aa / 67.3 kDa |
| UniProt ID | Q8N427 |
| 数据采集时间 | 2026-06-03 23:48:40 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Nuclear speckles, Primar; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 588 aa / 67.3 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=25 篇 (21-40 -> 8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=79.6; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR034907, IPR036850, IPR036249, IPR017937, I |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | -- | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **144.5/180** | |
| **归一化总分** | | | **80.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Nuclear speckles, Primary cilium | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 图像状态: if_display_images_available。

**GO Cellular Component**:
- axoneme (GO:0005930)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)
- outer dynein arm (GO:0036157)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SPTRX2, TXNDC3 |

**关键文献**:
1. Alzheimer's disease risk genes and mechanisms of disease pathogenesis.. *Biological psychiatry*. PMID: 24951455
2. Primary Ciliary Dyskinesia.. **. PMID: 20301301
3. Nuclear functions of NME proteins.. *Laboratory investigation; a journal of technical methods and pathology*. PMID: 29058704
4. NME8 rs2718058 polymorphism with Alzheimer's disease risk: a replication and meta-analysis.. *Oncotarget*. PMID: 27144521
5. iNPH-the mystery resolving.. *EMBO molecular medicine*. PMID: 33555136

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.6 |
| 高置信度残基 (pLDDT>90) 占比 | 31.0% |
| 置信残基 (pLDDT 70-90) 占比 | 52.9% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 11.9% |
| 有序区域 (pLDDT>70) 占比 | 83.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 中等质量（pLDDT=79.6，有序区 83.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034907, IPR036850, IPR036249, IPR017937, IPR013766; Pfam: PF00334, PF00085 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DNAI1 | 0.982 | 0.423 | — |
| DNAI2 | 0.981 | 0.423 | — |
| DNAH5 | 0.976 | 0.380 | — |
| DNAH11 | 0.942 | 0.380 | — |
| CCDC114 | 0.940 | 0.402 | — |
| RSPH4A | 0.917 | 0.174 | — |
| RSPH9 | 0.915 | 0.205 | — |
| DNAAF2 | 0.900 | 0.000 | — |
| DNAAF1 | 0.877 | 0.045 | — |
| DNAH1 | 0.867 | 0.380 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| REPIN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRIM23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IFT57 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| BACH1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| TRAF3IP1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| IFT20 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| POTEB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| VPS39 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000440017 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 9 / 15 = 60%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 60%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.6 + PDB: 无 | pLDDT=79.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nucleoplasm, Nuclear speckles, Primar | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. NME8 -- Protein NME8，非常新颖，仅有少数基础研究。
2. 蛋白大小588 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N427
- Protein Atlas: https://www.proteinatlas.org/ENSG00000086288-NME8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NME8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N427
- STRING: https://string-db.org/network/9606.NME8
- Packet data timestamp: 2026-06-03 23:48:40

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*
