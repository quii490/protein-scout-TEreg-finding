---
type: protein-evaluation
gene: "MOB1B"
date: 2026-06-03
tags: [protein-scout, nucleolus, re-evaluation, recovery]
status: scored
category: nucleolus
normalized_score: 70.2
raw_score: 128.5
nuclear_score: 7
---

## MOB1B 核蛋白评估报告 (Full Re-evaluation)


### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MOB1B / MOB4A, MOBKL1A |
| 蛋白名称 | MOB kinase activator 1B |
| 蛋白大小 | 216 aa / 25.1 kDa |
| UniProt ID | Q7L9L4 |
| PubMed (strict) | 22 |
| PubMed (broad) | 61 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; Cytosol; UniProt: Cytoplasm; Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 216 aa / 25.1 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (21-40→8) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.5，PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR005301, IPR036703; Pfam: PF03637 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners, IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/183** | |
| **归一化总分** | | | **70.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持，部分数据源提示非核定位但核信号主导。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 61 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MOB4A, MOBKL1A |

**关键文献**:
1. Cullin-associated and neddylation-dissociated protein 1 (CAND1) promotes cardiomyocyte proliferation and heart regeneration by enhancing the ubiquitinated degradation of Mps one binder kinase activator 1b (Mob1b).. *Cell death and differentiation*. PMID: 40555744
2. Human Mob1 proteins are required for cytokinesis by controlling microtubule stability.. *Journal of cell science*. PMID: 22454515
3. Structural basis for autoinhibition and its relief of MOB1 in the Hippo pathway.. *Scientific reports*. PMID: 27335147
4. MiR-743a-5p regulates differentiation of myoblast by targeting Mob1b in skeletal muscle development and regeneration.. *Genes & diseases*. PMID: 35685465
5. Roles of mammalian sterile 20-like kinase 2-dependent phosphorylations of Mps one binder 1B in the activation of nuclear Dbf2-related kinases.. *Genes to cells : devoted to molecular & cellular mechanisms*. PMID: 19919647

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.5 |
| 高置信度残基 (pLDDT>90) 占比 | 72.7% |
| 置信残基 (pLDDT 70-90) 占比 | 15.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 6.5% |
| 有序区域 (pLDDT>70) 占比 | 88.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 极高置信度预测（pLDDT=88.5，有序区 88.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005301, IPR036703; Pfam: PF03637 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LATS1 | 0.999 | 0.981 | — |
| LATS2 | 0.996 | 0.840 | — |
| MOB1A | 0.982 | 0.815 | — |
| STK3 | 0.972 | 0.623 | — |
| STK38L | 0.941 | 0.853 | — |
| SAV1 | 0.939 | 0.164 | — |
| STK4 | 0.920 | 0.503 | — |
| STK38 | 0.919 | 0.803 | — |
| WWTR1 | 0.790 | 0.071 | — |
| YAP1 | 0.786 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| O36610 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| LATS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:19739119|imex:IM-16954 |
| LATS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:19739119|imex:IM-16954 |
| ntpA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| STK4 | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-17872|pubmed:22863277 |
| STK38L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-20985|pubmed:24366813 |
| MOB1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-20985|pubmed:24366813 |
| HSD17B10 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| SOD1 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |

**已知复合体成员** (GO Cellular Component):
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.5 + PDB: 无 | pLDDT=88.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Nucleoli; Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MOB1B — MOB kinase activator 1B，非常新颖，仅有少数基础研究。
2. 蛋白大小216 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L9L4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173542-MOB1B
- Protein Atlas Subcellular: https://www.proteinatlas.org/ENSG00000173542-MOB1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MOB1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L9L4
- STRING: https://string-db.org/network
- IntAct: https://www.ebi.ac.uk/intact/search?query=MOB1B
- Packet data timestamp: 2026-06-03 21:49:15

---

*本报告基于最新的 harvest packet 数据（2026-06-03 21:49:15），各数据库实时抓取。评分严格遵循 /180 加权评分体系：核定位×4 + 大小×1 + 新颖性×5 + 结构×3 + 结构域×2 + PPI×3 + 互证加分（max+3）。PubMed>100 或 核定位≤3 为 REJECTED。*
