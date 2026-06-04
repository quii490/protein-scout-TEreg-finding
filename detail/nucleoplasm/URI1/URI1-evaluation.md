---
type: protein-evaluation
gene: "URI1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## URI1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | URI1 / C19orf2, NNX3, PPP1R19, RMP, URI |
| 蛋白名称 | Unconventional prefoldin RPB5 interactor 1 |
| 蛋白大小 | 535 aa / 59.8 kDa |
| UniProt ID | O94763 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm; Mitochondrion; Cell projection, dendrite |
| 蛋白大小 | 10/10 | ×1 | 10 | 535 aa / 59.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009053, IPR004127, IPR052255; Pfam: PF02996 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Mitochondrion; Cell projection, dendrite | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein folding chaperone complex (GO:0101031)
- RPAP3/R2TP/prefoldin-like complex (GO:1990062)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 75 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C19orf2, NNX3, PPP1R19, RMP, URI |

**关键文献**:
1. The Multiple Functions of the PAQosome: An R2TP- and URI1 Prefoldin-Based Chaperone Complex.. *Advances in experimental medicine and biology*. PMID: 30484152
2. HBx and c-MYC Cooperate to Induce URI1 Expression in HBV-Related Hepatocellular Carcinoma.. *International journal of molecular sciences*. PMID: 31739577
3. Potential of PAQosome as a therapeutic target for hepatic fibrosis.. *Journal of gastroenterology and hepatology*. PMID: 38016755
4. Control of transcription by Pontin and Reptin.. *Trends in cell biology*. PMID: 17320397
5. HOTAIR promotes myocardial fibrosis through regulating URI1 expression via Wnt pathway.. *European review for medical and pharmacological sciences*. PMID: 30402865

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.0 |
| 高置信度残基 (pLDDT>90) 占比 | 21.9% |
| 置信残基 (pLDDT 70-90) 占比 | 11.6% |
| 中等置信 (pLDDT 50-70) 占比 | 27.5% |
| 低置信 (pLDDT<50) 占比 | 39.1% |
| 有序区域 (pLDDT>70) 占比 | 33.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.0），有序残基占 33.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009053, IPR004127, IPR052255; Pfam: PF02996 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POLR2E | 0.999 | 0.874 | — |
| PFDN2 | 0.997 | 0.835 | — |
| UXT | 0.991 | 0.847 | — |
| RUVBL1 | 0.986 | 0.835 | — |
| PFDN6 | 0.982 | 0.798 | — |
| RUVBL2 | 0.978 | 0.833 | — |
| RPAP3 | 0.977 | 0.873 | — |
| PDRG1 | 0.973 | 0.779 | — |
| PPP1CC | 0.969 | 0.839 | — |
| WDR92 | 0.968 | 0.785 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| GTF2F2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| HSP90AA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19875381 |
| PPP1CC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21397856|imex:IM-15772 |
| ATF7 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| rph | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| PPP1R7 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PPP1CB | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PPP1CA | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.0 + PDB: 无 | pLDDT=62.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Mitochondrion; Cell projection / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. URI1 — Unconventional prefoldin RPB5 interactor 1，非常新颖，仅有少数基础研究。
2. 蛋白大小535 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94763
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105176-URI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=URI1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94763
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
