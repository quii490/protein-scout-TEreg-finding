---
type: protein-evaluation
gene: "METTL18"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## METTL18 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | METTL18 |
| 别名 | AsTP2, HPM1 |
| 基因全称 | methyltransferase 18 |
| 蛋白名称 | Histidine protein methyltransferase 1 homolog |
| 蛋白大小 | 372 aa |
| UniProt ID | O95568 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 8/10 | x4 | 32 | HPA: Nuclear bodies, Nucleoplasm |
| Size 蛋白大小 | 10/10 | x1 | 10 | 372 aa |
| Novelty 研究新颖性 | 10/10 | x5 | 50 | PubMed: 10 篇 |
| 3D Structure 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT=74.3 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 含甲基转移酶结构域，可能参与表观遗传调控 |
| PPI Network PPI网络 | 8/10 | x3 | 24 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +1.0 | — |
| **原始总分** |  |  | **152/183** |  |
| **归一化总分** |  |  | **83.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | U-251MG, A-431 | HPA validated |
| UniProt | Nucleus | — |
| GO-CC | GO:0005634 Nucleus (IBA|IEA) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/METTL18/IF_images/A_431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/METTL18/IF_images/U_251MG_1.jpg|U-251MG]]
#### 3.2 蛋白大小评估

372 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 10 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Kim HG et al. (2024). "METTL18 functions as a Phenotypic Regulator in Src-Dependent Oncogenic Responses of HER2-Negative Breast Cancer.". *Int J Biol Sci*. PMID: 39309445
2. Morshed MN et al. (2025). "Identification of novel small molecule inhibitors targeting multiple methyltransferase like proteins against hepatocellular carcinoma.". *Sci Rep*. PMID: 41006418
3. Kasai F et al. (2023). "γ-enolase (ENO2) is methylated at the Nτ position of His-190 among enolase isozymes.". *J Biochem*. PMID: 37279646
4. Małecki JM et al. (2021). "Human METTL18 is a histidine-specific methyltransferase that targets RPL3 and affects ribosome biogenesis and function.". *Nucleic Acids Res*. PMID: 33693809
5. Matsuura-Suzuki E et al. (2022). "METTL18-mediated histidine methylation of RPL3 modulates translation elongation for proteostasis maintenance.". *Elife*. PMID: 35674491


**评价**: PubMed 10 篇，属极度新颖蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 74.3 |
| pLDDT > 90 占比 | 49.7% |
| pLDDT 70-90 占比 | 12.4% |
| pLDDT 50-70 占比 | 8.6% |
| pLDDT < 50 占比 | 29.3% |
| 可用 PDB 条目 | 1 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/METTL18/METTL18-PAE.png]]

**评价**: AlphaFold 预测中等质量，部分区域有序 (AlphaFold v6, pLDDT=74.3, >90=50%, 70-90=12%, 50-70=9%, <50=29%. PDB entries: 4RFQ)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 含甲基转移酶结构域，可能参与表观遗传调控

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-716478|uniprotkb:Q8N4I9|uniprotkb:D3DSR1|ensembl:ENSP00000320017.3|ensembl:ENSP00000415491.2 | MI:0398(two hybrid pooling approach | PMID:pubmed:16169070|imex:IM-16517|mint:MINT-5217955 | — | — |
| intact:EBI-194639 | MI:0018(two hybrid) | PMID:pubmed:14605208|imex:IM-16524|mint:MINT-5216804 | — | — |
| intact:EBI-78473|uniprotkb:Q6MZQ9|uniprotkb:Q13511|uniprotkb:Q14276|uniprotkb:Q9NU51|uniprotkb:Q9UDZ7|uniprotkb:Q9UIS7|intact:EBI-28988800|uniprotkb:Q5T5H7|ensembl:ENSP00000206249.3|ensembl:ENSP00000342630.5|ensembl:ENSP00000387500.1|ensembl:ENSP00000405330.1 | MI:0676(tandem affinity purificatio | PMID:pubmed:31527615|imex:IM-26954 | — | — |
| intact:EBI-1751761|uniprotkb:O76007|uniprotkb:Q53XR5|uniprotkb:B7Z8F2|intact:EBI-11047712|ensembl:ENSP00000470248.1 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | — |
| intact:EBI-2210673|uniprotkb:Q16404|uniprotkb:Q5JS26|uniprotkb:Q96IP7|uniprotkb:Q9BU88|ensembl:ENSP00000338561.5|ensembl:ENSP00000470740.2|ensembl:ENSP00000478714.1 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| RPL3 | 0.0 | — | — |
| METTL21A | 0.0 | — | — |
| VCPKMT | 0.0 | — | — |
| METTL22 | 0.0 | — | — |
| ETFBKMT | 0.0 | — | — |
| METTL1 | 0.0 | — | — |
| GRWD1 | 0.0 | — | — |
| KIN | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 18
- 调控相关比例: 5/15 (33%)

**评价**: PPI 得分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=74.3, PDB=1 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/18/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nuclear bodies, Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- PDB+AlphaFold 双源确认 (+0.5)
- IntAct+STRING 双源确认 (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★ (4/5)

**核心优势**:
1. 极度新颖 (PubMed 10 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 结构预测置信度较高
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=METTL18
- Protein Atlas: https://www.proteinatlas.org/METTL18
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=METTL18
- UniProt: https://www.uniprot.org/uniprotkb/O95568
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95568


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[METTL18-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/METTL18/METTL18-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95568 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019410;IPR029063; |
| Pfam | PF13489; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000171806-METTL18/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RPL3 | Biogrid, Bioplex | true |
| FCGRT | Bioplex | false |
| IMPA1 | Bioplex | false |
| MND1 | Bioplex | false |
| PHKA2 | Bioplex | false |
| PTGES2 | Bioplex | false |
| SMAD4 | Bioplex | false |
| TAGAP | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
