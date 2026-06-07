---
type: protein-evaluation
gene: "ARGFX"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation, scored]
status: scored
_date: 2026-05-29
_notes: "PubMed=16 (<100) → 基线提升: 结4→5; 域10已超基线6; 无HPA IF→核=7; PDB查无结构"
---

## ARGFX 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ARGFX / Arginine-fifty homeobox |
| 蛋白大小 | 315 aa / 35.6 kDa |
| UniProt ID | A6NJG6 |
| 评估日期 | 2026-05-28 () / 2026-05-29 |

**IF 图像**: 暂无IF数据

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | **28** | UniProt+GO预测Nucleus; 无HPA IF; Homeobox TF保守→7 |

> **Protein Atlas IF**: 暂无数据（Pending cell analysis），核定位依据 UniProt + GO。

| 📏 蛋白大小 | 10/10 | ×1 | **10** | 315 aa / 35.6 kDa, 理想实验大小 |
|---|---|---|---|---|
| 🆕 研究新颖性 | 10/10 | ×5 | **50** | PubMed=16; 极度新颖 |
| 🏗️ 三维结构 | 5/10 | ×3 | **15** | pLDDT 56.7; 无PDB; 新颖基线5 |
| 🧬 调控结构域 | 10/10 | ×2 | **20** | Homeodomain(9库确认); 经典DNA-binding TF |
| 🔗 PPI | 4/10 | ×3 | **12** | TPRX1(0.808),DUXB(0.738),KLF17(0.602); 76.5%调控相关但全部text-mining→4 |
| ➕ 互证加分 | — | — | **+1.5** | >=9库结构域; GO染色质一致; >=2源定位; 进化保守 |
| **原始总分** |  |  | **136.5/183** |  |
| **归一化总分** |  |  | **74.6/100** |  |

#### 3.6 PPI 网络（四源综合）

**实验验证互作** (IntAct):
- **无实验互作记录** — ARGFX 未被 IntAct 收录，反映该蛋白极度新颖且未被系统互作研究覆盖

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---|---|---|---|
| TPRX1 | 0.808 | Homeobox TF, early embryo | ✅ |
| DUXB | 0.738 | Double homeobox TF | ✅ |
| KLF17 | 0.602 | Krueppel-like factor, TF | ✅ |
| Other PRD-like TFs | 0.4-0.5 | Homeobox transcription factors | ✅ |
| — | — | 76.5%调控相关但全为text-mining | ⚠️ |

**已知复合体成员** (GO Cellular Component):
- **Chromatin (GO:0000785)** — 直接注释染色质定位
- Nucleus (GO:0005634)

**PPI 互证分析**:
- IntAct: 无实验数据（极度新颖蛋白的特征）
- STRING: 邻居蛋白富集 homeobox TF (TPRX1, DUXB, KLF17等)，76.5%为转录调控相关 — 但全部来源于text-mining
- GO-CC: Chromatin 注释直接指向染色质定位（但需核实证据代码等级）
- 调控相关比例: ~76.5%（STRING邻居），但缺乏实验验证

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARGFX/ARGFX-PAE.png]]

**评价**: ARGFX 在 IntAct 中无任何实验互作记录，与其极度新颖（PubMed仅16篇）一致。GO-CC 中 "chromatin" 的注释是该蛋白的重要线索——直接表明其染色质定位。STRING 邻居蛋白高度富集 homeobox 转录因子，与其自身 homeodomain 身份吻合。所有互作均为 text-mining 推导，无实验验证，这是极度新颖蛋白的典型特征。PPI 评分维持 4（邻居高度富集调控因子但无实验验证）。

### X. 关键文献 (PubMed)

1. Guo Q et al. (2025). "Allelic transcriptomic profiling identifies the role of PRD-like homeobox genes in human embryonic-cleavage-stage arrest.". *Dev Cell*. PMID: 39809281
2. Madissoon E et al. (2016). "Characterization and target genes of nine human PRD-like homeobox domain genes expressed exclusively in early embryos.". *Sci Rep*. PMID: 27412763
3. Li G et al. (2010). "The origin and evolution of ARGFX homeobox loci in mammalian radiation.". *BMC Evol Biol*. PMID: 20565723
4. Lewin TD et al. (2022). "PRD-Class Homeobox Genes in Bovine Early Embryos: Function, Evolution, and Overlapping Roles.". *Mol Biol Evol*. PMID: 35512670
5. Töhönen V et al. (2015). "Novel PRD-like homeodomain transcription factors and retrotransposon elements in early human development.". *Nat Commun*. PMID: 26360614

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. **极度新颖**：仅 16 篇 PubMed，homeobox TF 的生化功能完全未被探索，发现空间极大
2. **明确的 DNA 结合域**：Homeodomain 被 9 个数据库确认，染色质调控功能预测明确
3. **理想实验大小**：315 aa 适合各类生化实验，表达纯化可行
4. **胚胎发育特异性表达**：可能在早期胚胎表观遗传重编程中发挥作用（类似 DUX/TPRX 家族）

**风险/不确定性**:
1. **结构质量偏低**：pLDDT 仅 56.7，80% 残基无序，可能难以获得稳定结构
2. **PPI 全无实验验证**：所有相互作用均来自文本挖掘，可能为假阳性
3. **表达水平低**：Protein Atlas 蛋白水平未检出，组织特异性高（仅骨髓/心肌），可能难以获取内源材料
4. **功能完全未知**：无任何功能验证实验，可能存在功能冗余或仅在特定发育窗口有作用

**下一步建议**:
- [ ] 克隆 ARGFX ORF 到哺乳动物表达载体，在 HEK293T 细胞中验证核定位（IF/GFP 融合）
- [ ] ChIP-seq 鉴定 ARGFX 的全基因组结合位点
- [ ] 在胚胎干细胞中建立诱导表达系统，检测转录组变化
- [ ] 通过 IP-MS 鉴定真正的相互作用蛋白

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NJG6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186103-ARGFX
- PubMed: 16 articles (search: "ARGFX")
- STRING: https://string-db.org (ARGFX, 9606)
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NJG6
- EBI Proteins API: https://www.ebi.ac.uk/proteins/api/proteins/A6NJG6


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ARGFX-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ARGFX/ARGFX-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A6NJG6 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001356;IPR017970;IPR009057; |
| Pfam | PF00046; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000186103-ARGFX/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
